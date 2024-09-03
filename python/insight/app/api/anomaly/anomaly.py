from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.api.anomaly.response.res import (ResBodyAnomalyDetectionOptions, AnomalyDetectionOptions,
                                          ResBodyAnomalyDetectionSettings)
from app.api.anomaly.utils.utils import AnomalySettingsService, get_db
from app.api.anomaly.response.res import ResBodyVoid
from app.api.anomaly.request.req import AnomalyDetectionTargetRegistration, AnomalyDetectionTargetUpdate
from config.ConfigManager import read_config

router = APIRouter()


@router.get("/anomaly-detection/options", response_model=ResBodyAnomalyDetectionOptions)
async def get_available_options_for_anomaly_detection():
    config_data = read_config("config/anomaly.ini")

    response = ResBodyAnomalyDetectionOptions(data=AnomalyDetectionOptions(**config_data))

    return response


@router.get("/anomaly-detection/settings", response_model=ResBodyAnomalyDetectionSettings)
async def get_all_anomaly_detection_settings(db: Session = Depends(get_db)):
    anomaly_setting_service = AnomalySettingsService(db=db)
    response = anomaly_setting_service.get_all_settings()
    return response


@router.post("/anomaly-detection/settings", response_model=ResBodyVoid)
async def register_anomaly_detection_target(body: AnomalyDetectionTargetRegistration, db: Session = Depends(get_db)):
    service = AnomalySettingsService(db=db)
    return service.create_setting(setting_data=body.dict())


@router.put("/anomaly-detection/settings/{settingSeq}", response_model=ResBodyVoid)
async def update_anomaly_detection_target(settingSeq: int, body: AnomalyDetectionTargetUpdate, db: Session = Depends(get_db)):
    service = AnomalySettingsService(db=db)
    return service.update_setting(setting_seq=settingSeq, update_data=body.dict())


@router.delete("/anomaly-detection/settings/{settingSeq}", response_model=ResBodyVoid)
async def delete_anomaly_detection_target(settingSeq: int, db: Session = Depends(get_db)):
    service = AnomalySettingsService(db=db)
    return service.delete_setting(setting_seq=settingSeq)


@router.get("/anomaly-detection/settings/nsId/{nsId}/target/{targetId}", response_model=ResBodyAnomalyDetectionSettings)
async def get_specific_anomaly_detection_target(nsId: str, targetId: str, db: Session = Depends(get_db)):
    service = AnomalySettingsService(db=db)
    return service.get_setting(ns_id=nsId, target_id=targetId)
