/**
  Generated Main Source File

  Company:
    Microchip Technology Inc.

  File Name:
    main.c

  Summary:
    This is the main file generated using PIC10 / PIC12 / PIC16 / PIC18 MCUs

  Description:
    This header file provides implementations for driver APIs for all modules selected in the GUI.
    Generation Information :
        Product Revision  :  PIC10 / PIC12 / PIC16 / PIC18 MCUs - 1.81.8
        Device            :  PIC18F26K83
        Driver Version    :  2.00
*/

/*
    (c) 2018 Microchip Technology Inc. and its subsidiaries. 
    
    Subject to your compliance with these terms, you may use Microchip software and any 
    derivatives exclusively with Microchip products. It is your responsibility to comply with third party 
    license terms applicable to your use of third party software (including open source software) that 
    may accompany Microchip software.
    
    THIS SOFTWARE IS SUPPLIED BY MICROCHIP "AS IS". NO WARRANTIES, WHETHER 
    EXPRESS, IMPLIED OR STATUTORY, APPLY TO THIS SOFTWARE, INCLUDING ANY 
    IMPLIED WARRANTIES OF NON-INFRINGEMENT, MERCHANTABILITY, AND FITNESS 
    FOR A PARTICULAR PURPOSE.
    
    IN NO EVENT WILL MICROCHIP BE LIABLE FOR ANY INDIRECT, SPECIAL, PUNITIVE, 
    INCIDENTAL OR CONSEQUENTIAL LOSS, DAMAGE, COST OR EXPENSE OF ANY KIND 
    WHATSOEVER RELATED TO THE SOFTWARE, HOWEVER CAUSED, EVEN IF MICROCHIP 
    HAS BEEN ADVISED OF THE POSSIBILITY OR THE DAMAGES ARE FORESEEABLE. TO 
    THE FULLEST EXTENT ALLOWED BY LAW, MICROCHIP'S TOTAL LIABILITY ON ALL 
    CLAIMS IN ANY WAY RELATED TO THIS SOFTWARE WILL NOT EXCEED THE AMOUNT 
    OF FEES, IF ANY, THAT YOU HAVE PAID DIRECTLY TO MICROCHIP FOR THIS 
    SOFTWARE.
*/

#include "mcc_generated_files/mcc.h"

void TMR0_stepISR()
{
    static uint16_t step = 0;
    step ++;
    if(step == 3500) 
    {
        DMA1CON1 = (DMA1CON1&~0x06)|0x04;
        DMA1SSA = (&SrcVarName0)+8;
    }
    if(step > 7000) 
    {
        step = 0;
        DMA1CON1 = (DMA1CON1&~0x06)|0x02;
        DMA1SSA = &SrcVarName0;
    }
}

/*
                         Main application
 */
void main(void)
{
    // Initialize the device
    SYSTEM_Initialize();
    
    TMR0_SetInterruptHandler (TMR0_stepISR);
    
    SrcVarName0[0] = 0x09;
    SrcVarName0[1] = 0x0C;
    SrcVarName0[2] = 0x06;
    SrcVarName0[3] = 0x03;
    SrcVarName0[4] = 0x09;
    SrcVarName0[5] = 0x0C;
    SrcVarName0[6] = 0x06;
    SrcVarName0[7] = 0x03;
    //SrcVarName0[0] = 0x09;
    //SrcVarName0[1] = 0x05;
    //SrcVarName0[2] = 0x06;
    //SrcVarName0[3] = 0x0A;
    //SrcVarName0[4] = 0x09;
    //SrcVarName0[5] = 0x05;
    //SrcVarName0[6] = 0x06;
    //SrcVarName0[7] = 0x0A;
    DMA1DSA= (volatile unsigned short)&PORTC; //DMA1 destination address

    // If using interrupts in PIC18 High/Low Priority Mode you need to enable the Global High and Low Interrupts
    // If using interrupts in PIC Mid-Range Compatibility Mode you need to enable the Global Interrupts
    // Use the following macros to:
    
    // Enable high priority global interrupts.
    INTERRUPT_GlobalInterruptHighEnable();

    // Enable low priority global interrupts.
    INTERRUPT_GlobalInterruptLowEnable();
    
    // Disable high priority global interrupts
    //INTERRUPT_GlobalInterruptHighDisable();

    // Disable low priority global interrupts.
    //INTERRUPT_GlobalInterruptLowDisable();

    while (1)
    {
        // Add your application code
    }
}
/**
 End of File
*/