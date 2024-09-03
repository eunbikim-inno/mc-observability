from sqlalchemy.orm import Session
from app.api.anomaly.model.models import AnomalyDetectionSettings


def repo_get_all_settings(db: Session):
    return db.query(AnomalyDetectionSettings).all()


def repo_get_specific_setting(db: Session, ns_id: str, target_id: str):
    return db.query(AnomalyDetectionSettings).filter_by(NAMESPACE_ID=ns_id, TARGET_ID=target_id).all()


def repo_create_setting(db: Session, setting_data: dict):
    new_setting = AnomalyDetectionSettings(**setting_data)
    db.add(new_setting)
    db.commit()
    db.refresh(new_setting)
    return new_setting


def repo_update_setting(db: Session, setting_seq: int, update_data: dict):
    setting = db.query(AnomalyDetectionSettings).filter_by(SEQ=setting_seq).first()
    if setting:
        for key, value in update_data.items():
            setattr(setting, key.upper(), value)
        db.commit()
        db.refresh(setting)
        return setting
    return None


def repo_delete_setting(db: Session, setting_seq: int):
    setting = db.query(AnomalyDetectionSettings).filter_by(SEQ=setting_seq).first()
    if setting:
        db.delete(setting)
        db.commit()
        return setting
    return None


def repo_check_duplicate(db: Session, setting_data: dict):
    return db.query(AnomalyDetectionSettings).filter_by(
        NAMESPACE_ID=setting_data['NAMESPACE_ID'],
        TARGET_ID=setting_data['TARGET_ID'],
        TARGET_TYPE=setting_data['TARGET_TYPE'],
        METRIC_TYPE=setting_data['METRIC_TYPE']
    ).first()
