def showProgramName( ) :
    print( '**-- โปรแกรมคำนวณค่า BMI --**')

def inputData( ) :
    weight = float(input('ป้อนน้ำหนัก(กิโลกรัม) : '))
    height = float(input('ป้อนส่วนสูง(เมตร) : '))
    return weight, height

def calBMI(weight,height) :
    BMI = weight / (height**2)
    return BMI

def showBMI (BMI,weight,height) :
    print('น้ำหนัก' , weight, 'กิโลกรัม' , 'สูง', height ,'เมตร', 'มีค่า BMI คือ', "{:.2f}".format(BMI))
    print('น้ำหนัก ' + str(weight) + ' กิโลกรัม ' +'สูง ' + str(height) + ' เมตร ' + 'มีค่า BMI คือ ' + str("{:.2f}".format(BMI)))
    print('น้ำหนัก {} กิโลกรัม สูง {} เมตร มีค่า BMI คือ {}'.format(weight, height, "{:.2f}".format(BMI)))
    print(f'น้ำหนัก {weight} กิโลกรัม สูง {height} เมตร มีค่า BMI คือ {"{:.2f}".format(BMI)}')

showProgramName( )
print('--------------------------------------')
weight,height = inputData( )
print('--------------------------------------')
BMI = calBMI(weight,height)
print('--------------------------------------')
showBMI (BMI,weight,height)
print('--------------------------------------')