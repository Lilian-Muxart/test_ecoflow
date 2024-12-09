from custom_components.ecoflow_cloud.api import EcoflowApiClient
from custom_components.ecoflow_cloud.devices import BaseDevice
from custom_components.ecoflow_cloud.entities import BaseSensorEntity, BaseNumberEntity, BaseSwitchEntity, BaseSelectEntity
from ...sensor import StatusSensorEntity, InWattsSolarSensorEntity, DecivoltSensorEntity, CentivoltSensorEntity, \
    DeciampSensorEntity, CelsiusSensorEntity, DecicelsiusSensorEntity, MiscSensorEntity, LevelSensorEntity, DeciwattsSensorEntity, \
    AmpSensorEntity, RemainSensorEntity, DecihertzSensorEntity, WattsSensorEntity, MilliVoltSensorEntity, TempSensorEntity, MiscBinarySensorEntity
from custom_components.ecoflow_cloud.switch import EnabledEntity

class Generator_DualFuel(BaseDevice):
    def sensors(self, client: EcoflowApiClient) -> list[BaseSensorEntity]:
        return [
            LevelSensorEntity(client, self, "pd.oilVal", name="Fuel Tank Level", device_class="battery", unit_of_measurement="%"),
            RemainSensorEntity(client, self, "pd.motorUseTime", name="Generator Working Duration", unit_of_measurement="minutes"),
            WattsSensorEntity(client, self, "pd.totalPower", name="Total Power", unit_of_measurement="W"),
            RemainSensorEntity(client, self, "pd.remainTime", name="Remaining Time", unit_of_measurement="minutes"),
            WattsSensorEntity(client, self, "pd.dcPower", name="DC Power", unit_of_measurement="W"),
            MilliVoltSensorEntity(client, self, "pd.dcVol", name="DC Voltage", unit_of_measurement="V"),
            AmpSensorEntity(client, self, "pd.dcCur", name="DC Charge Current", unit_of_measurement="A"),
            WattsSensorEntity(client, self, "pd.oilMaxOutPower", name="Oil Max Power", unit_of_measurement="W"),
            WattsSensorEntity(client, self, "pd.acPower", name="AC Power", unit_of_measurement="W"),
            MilliVoltSensorEntity(client, self, "pd.acVol", name="AC Voltage", unit_of_measurement="V"),
            AmpSensorEntity(client, self, "pd.acCur", name="AC Charge Current", unit_of_measurement="A"),
            TempSensorEntity(client, self, "pd.temp", name="Temperature", unit_of_measurement="°C"),
            MiscBinarySensorEntity(client, self, "pd.acState", name="AC State"),
            MiscBinarySensorEntity(client, self, "pd.dcOutState", name="DC Out State"),
            MiscBinarySensorEntity(client, self, "pd.motorState", name="Motor State"),
            StatusSensorEntity(client, self, "pd.sysMode", name="System Mode"),
            StatusSensorEntity(client, self, "pd.errCode", name="Error Code"),
            StatusSensorEntity(client, self, "pd.ver", name="Software Version"),
        ]

    def switches(self, client: EcoflowApiClient) -> list[BaseSwitchEntity]:
        return [
            EnabledEntity(client, self, "pd.motorUseTime", None,
                          lambda value: {"operateType": "motorCtrl", "params": {"enable": value}}),
                          
                          ]

    def numbers(self, client: EcoflowApiClient) -> list[BaseNumberEntity]:
        return []

    def selects(self, client: EcoflowApiClient) -> list[BaseSelectEntity]:
        return []
