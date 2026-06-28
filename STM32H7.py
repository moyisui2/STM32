import json


#导入外设介绍数据和定义数据
with open('DATA/STM32H7_DATA_D/STM32H7_WAISHE_DATA.json', 'r', encoding='utf-8') as f:
    WAISHE_DATA = json.load(f)
with open('DATA/STM32H7_DATA_D/STM32H7_Define.json', 'r', encoding='utf-8') as f:
    DEFINE_DATA = json.load(f)
with open('DATA/STM32H7_DATA_D/STM32H7_Define_X.json', 'r', encoding='utf-8') as f:
    DEFINE_DATA_DefineX = json.load(f)


#导入各个外设的函数数据
with open('DATA/STM32H7_DATA/ADC.json', 'r', encoding='utf-8') as f:
    ADC_DATA = json.load(f)
with open('DATA/STM32H7_DATA/ADCEX.json', 'r', encoding='utf-8') as f:
    ADCEX_DATA = json.load(f)
with open('DATA/STM32H7_DATA/CEC.json', 'r', encoding='utf-8') as f:
    CEC_DATA = json.load(f)
with open('DATA/STM32H7_DATA/COMP.json', 'r', encoding='utf-8') as f:
    COMP_DATA = json.load(f)
with open('DATA/STM32H7_DATA/CORTEX.json', 'r', encoding='utf-8') as f:
    CORTEX_DATA = json.load(f)
with open('DATA/STM32H7_DATA/CRC.json', 'r', encoding='utf-8') as f:
    CRC_DATA = json.load(f)
with open('DATA/STM32H7_DATA/CRCEX.json', 'r', encoding='utf-8') as f:
    CRCEX_DATA = json.load(f)
with open('DATA/STM32H7_DATA/CRYP.json', 'r', encoding='utf-8') as f:
    CRYP_DATA = json.load(f)
with open('DATA/STM32H7_DATA/CRYPEX.json', 'r', encoding='utf-8') as f:
    CRYPEX_DATA = json.load(f)
with open('DATA/STM32H7_DATA/DAC.json', 'r', encoding='utf-8') as f:
    DAC_DATA = json.load(f)
with open('DATA/STM32H7_DATA/DACEX.json', 'r', encoding='utf-8') as f:
    DACEX_DATA = json.load(f)
with open('DATA/STM32H7_DATA/DCMI.json', 'r', encoding='utf-8') as f:
    DCMI_DATA = json.load(f)
with open('DATA/STM32H7_DATA/DFSDM.json', 'r', encoding='utf-8') as f:
    DFSDM_DATA = json.load(f)
with open('DATA/STM32H7_DATA/DMA.json', 'r', encoding='utf-8') as f:
    DMA_DATA = json.load(f)
with open('DATA/STM32H7_DATA/DMA2D.json', 'r', encoding='utf-8') as f:
    DMA2D_DATA = json.load(f)
with open('DATA/STM32H7_DATA/DMAEX.json', 'r', encoding='utf-8') as f:
    DMAEX_DATA = json.load(f)
with open('DATA/STM32H7_DATA/ETH.json', 'r', encoding='utf-8') as f:
    ETH_DATA = json.load(f)
with open('DATA/STM32H7_DATA/ETHEX.json', 'r', encoding='utf-8') as f:
    ETHEX_DATA = json.load(f)
with open('DATA/STM32H7_DATA/EXTI.json', 'r', encoding='utf-8') as f:
    EXTI_DATA = json.load(f)
with open('DATA/STM32H7_DATA/FDCAN.json', 'r', encoding='utf-8') as f:
    FDCAN_DATA = json.load(f)
with open('DATA/STM32H7_DATA/FLASH.json', 'r', encoding='utf-8') as f:
    FLASH_DATA = json.load(f)
with open('DATA/STM32H7_DATA/FLASHEX.json', 'r', encoding='utf-8') as f:
    FLASHEX_DATA = json.load(f)
with open('DATA/STM32H7_DATA/GPIO.json', 'r', encoding='utf-8') as f:
    GPIO_DATA = json.load(f)
with open('DATA/STM32H7_DATA/HAL.json', 'r', encoding='utf-8') as f:
    HAL_DATA = json.load(f)
with open('DATA/STM32H7_DATA/HASH.json', 'r', encoding='utf-8') as f:
    HASH_DATA = json.load(f)
with open('DATA/STM32H7_DATA/HASHEX.json', 'r', encoding='utf-8') as f:
    HASHEX_DATA = json.load(f)
with open('DATA/STM32H7_DATA/HCD.json', 'r', encoding='utf-8') as f:
    HCD_DATA = json.load(f)
with open('DATA/STM32H7_DATA/HRTIM.json', 'r', encoding='utf-8') as f:
    HRTIM_DATA = json.load(f)
with open('DATA/STM32H7_DATA/HSEM.json', 'r', encoding='utf-8') as f:
    HSEM_DATA = json.load(f)
with open('DATA/STM32H7_DATA/I2C.json', 'r', encoding='utf-8') as f:
    I2C_DATA = json.load(f)
with open('DATA/STM32H7_DATA/I2CEX.json', 'r', encoding='utf-8') as f:
    I2CEX_DATA = json.load(f)
with open('DATA/STM32H7_DATA/I2S.json', 'r', encoding='utf-8') as f:
    I2S_DATA = json.load(f)
with open('DATA/STM32H7_DATA/IRDA.json', 'r', encoding='utf-8') as f:
    IRDA_DATA = json.load(f)
with open('DATA/STM32H7_DATA/IWDG.json', 'r', encoding='utf-8') as f:
    IWDG_DATA = json.load(f)
with open('DATA/STM32H7_DATA/JPEG.json', 'r', encoding='utf-8') as f:
    JPEG_DATA = json.load(f)
with open('DATA/STM32H7_DATA/LPTIM.json', 'r', encoding='utf-8') as f:
    LPTIM_DATA = json.load(f)
with open('DATA/STM32H7_DATA/LTDC.json', 'r', encoding='utf-8') as f:
    LTDC_DATA = json.load(f)
with open('DATA/STM32H7_DATA/MDIOS.json', 'r', encoding='utf-8') as f:
    MDIOS_DATA = json.load(f)
with open('DATA/STM32H7_DATA/MDMA.json', 'r', encoding='utf-8') as f:
    MDMA_DATA = json.load(f)
with open('DATA/STM32H7_DATA/MMC.json', 'r', encoding='utf-8') as f:
    MMC_DATA = json.load(f)
with open('DATA/STM32H7_DATA/MMCEX.json', 'r', encoding='utf-8') as f:
    MMCEX_DATA = json.load(f)
with open('DATA/STM32H7_DATA/NAND.json', 'r', encoding='utf-8') as f:
    NAND_DATA = json.load(f)
with open('DATA/STM32H7_DATA/NOR.json', 'r', encoding='utf-8') as f:
    NOR_DATA = json.load(f)
with open('DATA/STM32H7_DATA/OPAMP.json', 'r', encoding='utf-8') as f:
    OPAMP_DATA = json.load(f)
with open('DATA/STM32H7_DATA/PCD.json', 'r', encoding='utf-8') as f:
    PCD_DATA = json.load(f)
with open('DATA/STM32H7_DATA/PCDEX.json', 'r', encoding='utf-8') as f:
    PCDEX_DATA = json.load(f)
with open('DATA/STM32H7_DATA/PWR.json', 'r', encoding='utf-8') as f:
    PWR_DATA = json.load(f)
with open('DATA/STM32H7_DATA/PWREX.json', 'r', encoding='utf-8') as f:
    PWREX_DATA = json.load(f)
with open('DATA/STM32H7_DATA/QSPI.json', 'r', encoding='utf-8') as f:
    QSPI_DATA = json.load(f)
with open('DATA/STM32H7_DATA/RAMECC.json', 'r', encoding='utf-8') as f:
    RAMECC_DATA = json.load(f)
with open('DATA/STM32H7_DATA/RCC.json', 'r', encoding='utf-8') as f:
    RCC_DATA = json.load(f)
with open('DATA/STM32H7_DATA/RCCEX.json', 'r', encoding='utf-8') as f:
    RCCEX_DATA = json.load(f)
with open('DATA/STM32H7_DATA/RNG.json', 'r', encoding='utf-8') as f:
    RNG_DATA = json.load(f)
with open('DATA/STM32H7_DATA/RTC.json', 'r', encoding='utf-8') as f:
    RTC_DATA = json.load(f)
with open('DATA/STM32H7_DATA/RTCEX.json', 'r', encoding='utf-8') as f:
    RTCEX_DATA = json.load(f)
with open('DATA/STM32H7_DATA/SAI.json', 'r', encoding='utf-8') as f:
    SAI_DATA = json.load(f)
with open('DATA/STM32H7_DATA/SAIEX.json', 'r', encoding='utf-8') as f:
    SAIEX_DATA = json.load(f)
with open('DATA/STM32H7_DATA/SDEX.json', 'r', encoding='utf-8') as f:
    SDEX_DATA = json.load(f)
with open('DATA/STM32H7_DATA/SDIO.json', 'r', encoding='utf-8') as f:
    SDIO_DATA = json.load(f)
with open('DATA/STM32H7_DATA/SDRAM.json', 'r', encoding='utf-8') as f:
    SDRAM_DATA = json.load(f)
with open('DATA/STM32H7_DATA/SMARTCARD.json', 'r', encoding='utf-8') as f:
    SMARTCARD_DATA = json.load(f)
with open('DATA/STM32H7_DATA/SMARTCARDEX.json', 'r', encoding='utf-8') as f:
    SMARTCARDEX_DATA = json.load(f)
with open('DATA/STM32H7_DATA/SMBUS.json', 'r', encoding='utf-8') as f:
    SMBUS_DATA = json.load(f)
with open('DATA/STM32H7_DATA/SMBUSEX.json', 'r', encoding='utf-8') as f:
    SMBUSEX_DATA = json.load(f)
with open('DATA/STM32H7_DATA/SPDIFRX.json', 'r', encoding='utf-8') as f:
    SPDIFRX_DATA = json.load(f)
with open('DATA/STM32H7_DATA/SPI.json', 'r', encoding='utf-8') as f:
    SPI_DATA = json.load(f)
with open('DATA/STM32H7_DATA/SPIEX.json', 'r', encoding='utf-8') as f:
    SPIEX_DATA = json.load(f)
with open('DATA/STM32H7_DATA/SRAM.json', 'r', encoding='utf-8') as f:
    SRAM_DATA = json.load(f)
with open('DATA/STM32H7_DATA/SWPMI.json', 'r', encoding='utf-8') as f:
    SWPMI_DATA = json.load(f)
with open('DATA/STM32H7_DATA/TIM.json', 'r', encoding='utf-8') as f:
    TIM_DATA = json.load(f)
with open('DATA/STM32H7_DATA/TIMEX.json', 'r', encoding='utf-8') as f:
    TIMEX_DATA = json.load(f)
with open('DATA/STM32H7_DATA/UART.json', 'r', encoding='utf-8') as f:
    UART_DATA = json.load(f)
with open('DATA/STM32H7_DATA/UARTEX.json', 'r', encoding='utf-8') as f:
    UARTEX_DATA = json.load(f)
with open('DATA/STM32H7_DATA/USART.json', 'r', encoding='utf-8') as f:
    USART_DATA = json.load(f)
with open('DATA/STM32H7_DATA/USARTEX.json', 'r', encoding='utf-8') as f:
    USARTEX_DATA = json.load(f)
with open('DATA/STM32H7_DATA/WWDG.json', 'r', encoding='utf-8') as f:
    WWDG_DATA = json.load(f)
with open('DATA/STM32H7_DATA/SD.json', 'r', encoding='utf-8') as f:
    SD_DATA = json.load(f)
with open('DATA/STM32H7_DATA/OPAMPEX.json', 'r', encoding='utf-8') as f:
    OPAMPEX_DATA = json.load(f)





#合并外设函数数据
WW_DATA={
    "ADC":list(ADC_DATA.keys()) + list(ADCEX_DATA.keys()),
    "CEC":list(CEC_DATA.keys()),
    "COMP":list(COMP_DATA.keys()),
    "CORTEX":list(CORTEX_DATA.keys()),
    "CRC":list(CRC_DATA.keys()) + list(CRCEX_DATA.keys()),
    "CRYP":list(CRYP_DATA.keys()) + list(CRYPEX_DATA.keys()),
    "DAC":list(DAC_DATA.keys()) + list(DACEX_DATA.keys()),
    "DCMI":list(DCMI_DATA.keys()),
    "DFSDM":list(DFSDM_DATA.keys()),
    "DMA2D":list(DMA2D_DATA.keys()),
    "DMA":list(DMA_DATA.keys()) + list(DMAEX_DATA.keys()),
    "ETH":list(ETH_DATA.keys()) + list(ETHEX_DATA.keys()),
    "EXTI":list(EXTI_DATA.keys()),
    "FDCAN":list(FDCAN_DATA.keys()),
    "FLASH":list(FLASH_DATA.keys()) + list(FLASHEX_DATA.keys()),
    "GPIO":list(GPIO_DATA.keys()),
    "HAL":list(HAL_DATA.keys()),
    "HASH":list(HASH_DATA.keys()) + list(HASHEX_DATA.keys()),
    "HCD":list(HCD_DATA.keys()),
    "HRTIM":list(HRTIM_DATA.keys()),
    "HSEM":list(HSEM_DATA.keys()),
    "I2C":list(I2C_DATA.keys()) + list(I2CEX_DATA.keys()),
    "I2S":list(I2S_DATA.keys()),
    "IRDA":list(IRDA_DATA.keys()),
    "IWDG":list(IWDG_DATA.keys()),
    "JPEG":list(JPEG_DATA.keys()),
    "LPTIM":list(LPTIM_DATA.keys()),
    "LTDC":list(LTDC_DATA.keys()),
    "MDIOS":list(MDIOS_DATA.keys()),
    "MDMA":list(MDMA_DATA.keys()),
    "MMC":list(MMC_DATA.keys()) + list(MMCEX_DATA.keys()),
    "NOR":list(NOR_DATA.keys()),
    "NAND":list(NAND_DATA.keys()),
    "OPAMP":list(OPAMP_DATA.keys()),
    "PCD":list(PCD_DATA.keys()) + list(PCDEX_DATA.keys()),
    "PWR":list(PWR_DATA.keys()) + list(PWREX_DATA.keys()),
    "QSPI":list(QSPI_DATA.keys()),
    "RAMECC":list(RAMECC_DATA.keys()),
    "RCC":list(RCC_DATA.keys()) + list(RCCEX_DATA.keys()),
    "RNG":list(RNG_DATA.keys()),
    "RTC":list(RTC_DATA.keys()) + list(RTCEX_DATA.keys()),
    "SAI":list(SAI_DATA.keys()) + list(SAIEX_DATA.keys()),
    "SDRAM":list(SDRAM_DATA.keys()),
    "SDIO":list(SDIO_DATA.keys()),
    "SMARTCARD":list(SMARTCARD_DATA.keys()) + list(SMARTCARDEX_DATA.keys()),
    "SMBUS":list(SMBUS_DATA.keys()) + list(SMBUSEX_DATA.keys()),
    "SPDIFRX":list(SPDIFRX_DATA.keys()),
    "SPI":list(SPI_DATA.keys()) + list(SPIEX_DATA.keys()),
    "SRAM":list(SRAM_DATA.keys()),
    "SWPMI":list(SWPMI_DATA.keys()),
    "TIM":list(TIM_DATA.keys()) + list(TIMEX_DATA.keys()),
    "UART":list(UART_DATA.keys()) + list(UARTEX_DATA.keys()),
    "USART":list(USART_DATA.keys()) + list(USARTEX_DATA.keys()),
    "WWDG":list(WWDG_DATA.keys()),
    "SD":list(SDEX_DATA.keys()) + list(SD_DATA.keys()),
    "OPAMP":list(OPAMP_DATA.keys()) + list(OPAMPEX_DATA.keys())
}



ALL_STM32H7_DATA = {
    **ADC_DATA, **ADCEX_DATA, **CEC_DATA, **COMP_DATA, **CORTEX_DATA, **CRC_DATA, **CRCEX_DATA,
    **CRYP_DATA, **CRYPEX_DATA, **DAC_DATA, **DACEX_DATA, **DCMI_DATA, **DFSDM_DATA, **DMA_DATA,
    **DMA2D_DATA, **DMAEX_DATA, **ETH_DATA, **ETHEX_DATA, **EXTI_DATA, **FDCAN_DATA, **FLASH_DATA,
    **FLASHEX_DATA, **GPIO_DATA, **HAL_DATA, **HASH_DATA, **HASHEX_DATA, **HCD_DATA, **HRTIM_DATA,
    **HSEM_DATA, **I2C_DATA, **I2CEX_DATA, **I2S_DATA, **IRDA_DATA, **IWDG_DATA, **JPEG_DATA,
    **LPTIM_DATA, **LTDC_DATA, **MDIOS_DATA, **MDMA_DATA, **MMC_DATA, **MMCEX_DATA, **NAND_DATA,
    **NOR_DATA, **OPAMP_DATA, **PCD_DATA, **PCDEX_DATA, **PWR_DATA, **PWREX_DATA,
    **QSPI_DATA, **RAMECC_DATA, **RCC_DATA, **RCCEX_DATA, **RNG_DATA, **RTC_DATA, **RTCEX_DATA,
    **SAI_DATA, **SAIEX_DATA, **SDEX_DATA, **SDIO_DATA, **SDRAM_DATA, **SMARTCARD_DATA,
    **SMARTCARDEX_DATA, **SMBUS_DATA, **SMBUSEX_DATA, **SPDIFRX_DATA, **SPI_DATA, **SPIEX_DATA,
    **SRAM_DATA, **SWPMI_DATA, **TIM_DATA, **TIMEX_DATA, **UART_DATA, **UARTEX_DATA,
    **USART_DATA, **USARTEX_DATA, **WWDG_DATA, **SD_DATA, **OPAMPEX_DATA,**DEFINE_DATA
}

ALL_STM32H7_DATA_H = {
    **ADC_DATA, **ADCEX_DATA, **CEC_DATA, **COMP_DATA, **CORTEX_DATA, **CRC_DATA, **CRCEX_DATA,
    **CRYP_DATA, **CRYPEX_DATA, **DAC_DATA, **DACEX_DATA, **DCMI_DATA, **DFSDM_DATA, **DMA_DATA,
    **DMA2D_DATA, **DMAEX_DATA, **ETH_DATA, **ETHEX_DATA, **EXTI_DATA, **FDCAN_DATA, **FLASH_DATA,
    **FLASHEX_DATA, **GPIO_DATA, **HAL_DATA, **HASH_DATA, **HASHEX_DATA, **HCD_DATA, **HRTIM_DATA,
    **HSEM_DATA, **I2C_DATA, **I2CEX_DATA, **I2S_DATA, **IRDA_DATA, **IWDG_DATA, **JPEG_DATA,
    **LPTIM_DATA, **LTDC_DATA, **MDIOS_DATA, **MDMA_DATA, **MMC_DATA, **MMCEX_DATA, **NAND_DATA,
    **NOR_DATA, **OPAMP_DATA, **PCD_DATA, **PCDEX_DATA, **PWR_DATA, **PWREX_DATA,
    **QSPI_DATA, **RAMECC_DATA, **RCC_DATA, **RCCEX_DATA, **RNG_DATA, **RTC_DATA, **RTCEX_DATA,
    **SAI_DATA, **SAIEX_DATA, **SDEX_DATA, **SDIO_DATA, **SDRAM_DATA, **SMARTCARD_DATA,
    **SMARTCARDEX_DATA, **SMBUS_DATA, **SMBUSEX_DATA, **SPDIFRX_DATA, **SPI_DATA, **SPIEX_DATA,
    **SRAM_DATA, **SWPMI_DATA, **TIM_DATA, **TIMEX_DATA, **UART_DATA, **UARTEX_DATA,
    **USART_DATA, **USARTEX_DATA, **WWDG_DATA, **SD_DATA, **OPAMPEX_DATA
}