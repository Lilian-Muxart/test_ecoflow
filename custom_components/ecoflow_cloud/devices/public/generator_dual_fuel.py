from custom_components.ecoflow_cloud.api import EcoflowApiClient
from custom_components.ecoflow_cloud.devices import BaseDevice, const
from custom_components.ecoflow_cloud.entities import BaseSensorEntity, BaseNumberEntity, BaseSwitchEntity, BaseSelectEntity
from ...sensor import StatusSensorEntity, InWattsSolarSensorEntity, DecivoltSensorEntity, CentivoltSensorEntity, \
    DeciampSensorEntity, CelsiusSensorEntity, DecicelsiusSensorEntity, MiscSensorEntity, LevelSensorEntity, DeciwattsSensorEntity, \
    AmpSensorEntity, RemainSensorEntity, DecihertzSensorEntity, WattsSensorEntity, MilliVoltSensorEntity, TempSensorEntity, MiscBinarySensorEntity
from custom_components.ecoflow_cloud.switch import EnabledEntity

class Generator_DualFuel(BaseDevice):
    def sensors(self, client: EcoflowApiClient) -> list[BaseSensorEntity]:
        return [

            MiscBinarySensorEntity(client, self, "pd.motorState", const.MOTOR_STATE),
            RemainSensorEntity(client, self, "pd.motorUseTime", const.MOTOR_USE_TIME),
            LevelSensorEntity(client, self, "pd.oilVal", const.FUEL_LEVEL),
            MiscSensorEntity(client, self, "pd.errCode", const.ERROR_CODE),  # Ajout de MiscSensorEntity
        ]

    def switches(self, client: EcoflowApiClient) -> list[BaseSwitchEntity]:
        return [
            EnabledEntity(client, self, "pd.motorCtrl", const.MOTOR_ENABLED,
                          lambda value: {"operateType": "motorCtrl", "params": {"enable": value}}),
                          
                          ]

    def numbers(self, client: EcoflowApiClient) -> list[BaseNumberEntity]:
        return []

    def selects(self, client: EcoflowApiClient) -> list[BaseSelectEntity]:
        return []
