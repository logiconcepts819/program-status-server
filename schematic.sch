v 20130925 2
C 40000 40000 0 0 0 title-B.sym
C 50300 49400 1 0 0 3.3V-plus-1.sym
C 49300 46500 1 0 0 gnd-1.sym
C 50600 47100 1 90 0 resistor-1.sym
{
T 50200 47400 5 10 0 0 90 0 1
device=RESISTOR
T 50300 47400 5 10 1 1 90 0 1
refdes=R3
T 50700 47400 5 10 1 1 0 0 1
value=1kΩ
}
C 48400 47100 1 90 0 resistor-1.sym
{
T 48000 47400 5 10 0 0 90 0 1
device=RESISTOR
T 48100 47400 5 10 1 1 90 0 1
refdes=R2
T 48500 47400 5 10 1 1 0 0 1
value=200Ω
}
C 48100 49500 1 270 0 led-1.sym
{
T 48700 48700 5 10 0 0 270 0 1
device=LED
T 48500 48700 5 10 1 1 270 0 1
refdes=LED2
T 48900 48700 5 10 0 0 270 0 1
symversion=0.1
}
C 50500 48700 1 90 0 switch-spst-1.sym
{
T 49800 49100 5 10 0 0 90 0 1
device=SPST
T 50200 49000 5 10 1 1 90 0 1
refdes=S1
}
C 51100 48600 1 0 0 output-1.sym
{
T 51200 48900 5 10 0 0 0 0 1
device=OUTPUT
T 52000 48600 5 10 1 1 0 0 1
value=GPIO input (GPIO22)
}
C 47500 49400 1 0 0 input-1.sym
{
T 47500 49700 5 10 0 0 0 0 1
device=INPUT
T 46100 49700 5 10 1 1 0 0 1
value=GPIO output (GPIO21)
}
N 45700 46800 50500 46800 4
N 51100 48700 50500 48700 4
N 50500 48000 50500 48700 4
N 48300 48000 48300 48600 4
N 48300 46800 48300 47100 4
N 50500 47100 50500 46800 4
C 45800 47100 1 90 0 resistor-1.sym
{
T 45400 47400 5 10 0 0 90 0 1
device=RESISTOR
T 45500 47400 5 10 1 1 90 0 1
refdes=R1
T 45900 47400 5 10 1 1 0 0 1
value=200Ω
}
C 45500 49500 1 270 0 led-1.sym
{
T 46100 48700 5 10 0 0 270 0 1
device=LED
T 46300 48700 5 10 0 0 270 0 1
symversion=0.1
T 45900 48700 5 10 1 1 270 0 1
refdes=LED1
}
C 44900 49400 1 0 0 input-1.sym
{
T 44900 49700 5 10 0 0 0 0 1
device=INPUT
T 43700 49700 5 10 1 1 0 0 1
value=GPIO output (GPIO17)
}
N 45700 48000 45700 48600 4
N 45700 46800 45700 47100 4
C 50300 45700 1 0 0 3.3V-plus-1.sym
C 49300 42800 1 0 0 gnd-1.sym
C 50600 43400 1 90 0 resistor-1.sym
{
T 50200 43700 5 10 0 0 90 0 1
device=RESISTOR
T 50300 43700 5 10 1 1 90 0 1
refdes=R6
T 50700 43700 5 10 1 1 0 0 1
value=1kΩ
}
C 48400 43400 1 90 0 resistor-1.sym
{
T 48000 43700 5 10 0 0 90 0 1
device=RESISTOR
T 48100 43700 5 10 1 1 90 0 1
refdes=R5
T 48500 43700 5 10 1 1 0 0 1
value=200Ω
}
C 48100 45800 1 270 0 led-1.sym
{
T 48700 45000 5 10 0 0 270 0 1
device=LED
T 48900 45000 5 10 0 0 270 0 1
symversion=0.1
T 48500 45000 5 10 1 1 270 0 1
refdes=LED4
}
C 50500 45000 1 90 0 switch-spst-1.sym
{
T 49800 45400 5 10 0 0 90 0 1
device=SPST
T 50200 45300 5 10 1 1 90 0 1
refdes=S2
}
C 51100 44900 1 0 0 output-1.sym
{
T 51200 45200 5 10 0 0 0 0 1
device=OUTPUT
T 52000 44900 5 10 1 1 0 0 1
value=GPIO input (GPIO25)
}
C 47500 45700 1 0 0 input-1.sym
{
T 47500 46000 5 10 0 0 0 0 1
device=INPUT
T 46100 46000 5 10 1 1 0 0 1
value=GPIO output (GPIO24)
}
N 45700 43100 50500 43100 4
N 51100 45000 50500 45000 4
N 50500 44300 50500 45000 4
N 48300 44300 48300 44900 4
N 48300 43100 48300 43400 4
N 50500 43400 50500 43100 4
C 45800 43400 1 90 0 resistor-1.sym
{
T 45400 43700 5 10 0 0 90 0 1
device=RESISTOR
T 45500 43700 5 10 1 1 90 0 1
refdes=R4
T 45900 43700 5 10 1 1 0 0 1
value=200Ω
}
C 45500 45800 1 270 0 led-1.sym
{
T 46100 45000 5 10 0 0 270 0 1
device=LED
T 46300 45000 5 10 0 0 270 0 1
symversion=0.1
T 45900 45000 5 10 1 1 270 0 1
refdes=LED3
}
C 44900 45700 1 0 0 input-1.sym
{
T 44900 46000 5 10 0 0 0 0 1
device=INPUT
T 43700 46000 5 10 1 1 0 0 1
value=GPIO output (GPIO23)
}
N 45700 44300 45700 44900 4
N 45700 43100 45700 43400 4
N 50500 49500 50500 49400 4
N 50500 45800 50500 45700 4
