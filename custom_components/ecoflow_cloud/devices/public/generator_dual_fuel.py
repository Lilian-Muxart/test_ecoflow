from custom_components.ecoflow_cloud.api import EcoflowApiClient
from custom_components.ecoflow_cloud.devices import BaseDevice, const
from custom_components.ecoflow_cloud.entities import BaseSensorEntity, BaseNumberEntity, BaseSwitchEntity, BaseSelectEntity
from ...sensor import StatusSensorEntity, InWattsSolarSensorEntity, DecivoltSensorEntity, CentivoltSensorEntity, \
    DeciampSensorEntity, CelsiusSensorEntity, DecicelsiusSensorEntity, MiscSensorEntity, LevelSensorEntity, DeciwattsSensorEntity, \
    AmpSensorEntity, RemainSensorEntity, DecihertzSensorEntity, WattsSensorEntity, MilliVoltSensorEntity, TempSensorEntity, MiscBinarySensorEntity,  VoltSensorEntity
from custom_components.ecoflow_cloud.switch import EnabledEntity
from ...number import ChargingPowerEntity

class Generator_DualFuel(BaseDevice):
    def sensors(self, client: EcoflowApiClient) -> list[BaseSensorEntity]:
        return [

            MiscBinarySensorEntity(client, self, "pd.motorState", const.MOTOR_STATE),
            RemainSensorEntity(client, self, "pd.motorUseTime", const.MOTOR_USE_TIME),
            LevelSensorEntity(client, self, "pd.oilVal", const.FUEL_LEVEL),
            MiscSensorEntity(client, self, "pd.errCode", const.ERROR_CODE),
            MiscSensorEntity(client, self, "pd.ver", const.SOFTWARE_VERSION),
            WattsSensorEntity(client, self, "pd.totalPower", const.TOTAL_OUT_POWER),
            WattsSensorEntity(client, self, "pd.acPower", const.AC_OUT_POWER),
            WattsSensorEntity(client, self, "pd.dcPower", const.DC_OUT_POWER), 
            RemainSensorEntity(client, self, "pd.remainTime", const.REMAINING_TIME),
            VoltSensorEntity(client, self, "pd.dcVol", const.DC_OUT_VOLTAGE),
            VoltSensorEntity(client, self, "pd.acVol", const.AC_OUT_VOLT),
            CelsiusSensorEntity(client, self, "pd.temp", const.TEMPERATURE),
            #AmpSensorEntity(client, self, "pd.dcCur", const.DC_OUT_),
            #AmpSensorEntity(client, self, "pd.acCur", const.AC_OUT_CURRENT),
        ]

    def switches(self, client: EcoflowApiClient) -> list[BaseSwitchEntity]:
        return [
            EnabledEntity(client, self, "pd.motorState", const.MOTOR_ENABLED,
                          lambda value: {"isMatter": 0,"moduleType": 2,"operateType": "motorCtrl", "params": {"enable": value}}),
            EnabledEntity(client, self, "pd.sysMode", const.MOTOR_ECO,
                          lambda value: {"isMatter": 0,"moduleType": 2, "operateType": "modeCtrl", "params": {"mode": value}}),
                          
        ]

    def numbers(self, client: EcoflowApiClient) -> list[BaseNumberEntity]:
        return [
            ChargingPowerEntity(client, self, "pd.oilMaxOutPower","Max Oil Output Power", 1000, 1800,  
                lambda value: {"isMatter": 0, "moduleType": 2, "operateType": "oilMaxOutPower", "params": {"oilMax": value}}),
        
        ]

    def selects(self, client: EcoflowApiClient) -> list[BaseSelectEntity]:
        return []
