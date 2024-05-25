package mcmp.mc.observability.agent.controller;

import io.swagger.annotations.ApiOperation;
import lombok.RequiredArgsConstructor;
import mcmp.mc.observability.agent.annotation.Base64Decode;
import mcmp.mc.observability.agent.annotation.Base64Encode;
import mcmp.mc.observability.agent.common.Constants;
import mcmp.mc.observability.agent.model.MetricDataParamInfo;
import mcmp.mc.observability.agent.model.MetricInfo;
import mcmp.mc.observability.agent.model.MetricParamInfo;
import mcmp.mc.observability.agent.model.dto.HostStorageCreateDTO;
import mcmp.mc.observability.agent.model.dto.ResBody;
import mcmp.mc.observability.agent.service.MetricService;
import org.springframework.web.bind.annotation.*;

import javax.validation.Valid;
import java.util.List;

@RestController
@RequestMapping(Constants.PREFIX_V1 + "/metric")
@RequiredArgsConstructor
public class MetricController {

    private final MetricService metricService;

    @ApiOperation(value = "Get metrics")
    @GetMapping("")
    public ResBody<List<MetricInfo>> getMetrics(@Valid @ModelAttribute MetricParamInfo metricParamInfo) {
        ResBody<List<MetricInfo>> res = new ResBody<>();
        res.setData(metricService.getMetrics(metricParamInfo));
        return res;
    }

    @ApiOperation(value = "Get metrics with function")
    @GetMapping("/function")
    public ResBody<List<MetricInfo>> getMetricDatas(@Valid @ModelAttribute MetricDataParamInfo metricDataParamInfo) {
        ResBody<List<MetricInfo>> res = new ResBody<>();
        res.setData(metricService.getMetricDatas(metricDataParamInfo));
        return res;
    }


}
