import sms
import sim
import utime
from machine import Pin

class SmsLed:
    def __init__(self):
        self.led1 = Pin(Pin.GPIO11, Pin.OUT, Pin.PULL_DISABLE, 0)
        self.led2 = Pin(Pin.GPIO14, Pin.OUT, Pin.PULL_DISABLE, 0)
        self.setup()
        self.getnumber()

    def getdata(self):
        try:
            TextMsg = sms.searchTextMsg(0)
            if TextMsg == -1:
                return -1
            print("短信内容:", TextMsg[1])
            return TextMsg
        except Exception as e:
            print("获取短信失败:", e)
            return -1


    def control_select(self, device_id, action):
        if device_id == 'L1':
            if action == 'ON':
                self.led1.write(1)  # 开灯
            elif action == 'OFF':
                self.led1.write(0)  # 关灯
        elif device_id == 'L2':
            if action == 'ON':
                self.led2.write(1)  # 开灯
            elif action == 'OFF':
                self.led2.write(0)  # 关灯
            


    def parse_sms(self, msg):
        try:
            number = msg[0]# 解包元组
            content = msg[1]
            print("Received SMS from:", number)
            print("SMS content:", content)
            
            parts = content.split()
            if len(parts) < 3:
                self.send_response(number, "无效指令")
                return -1
            
            command, device_id, action = parts[0], parts[1], parts[2]
            if command == 'LIGHT':
                self.control_select(device_id, action)
                self.send_response(number, content)
            else:
                self.send_response(number, "无效指令")
                
            # 删除已处理短信
            sms.deleteMsg(1, 4)
        except Exception as e:
            print("处理短信异常:", e)

    def send_response(self, number, text):
        try:
            full_number = "+86" + number
            sms.sendTextMsg(full_number, text, "UCS2")
            print("已发送回复至", full_number)
        except Exception as e:
            print("短信发送失败:", e)

    def sms_callback(self, args):
        index = args[1]
        storage = args[2]
        print('New message! storage:{},index:{}'.format(storage, index))

    def setup(self):
        start=sms.setCallback(self.sms_callback)  
        sms.setSaveLoc("SM",'SM',"SM")      
        print("短信控制服务已启动",start)

    def getnumber(self):
        try:
            number = sim.getPhoneNumber()
            print("SIM卡号码:", number)
        except Exception as e:
            print("获取SIM卡号码失败:", e)

if __name__ == "__main__":
    sms.deleteMsg(1, 4)
    SMSLED = SmsLed()
    utime.sleep(3)
    while True:
        ret = SMSLED.getdata()
        if ret != -1:
            SMSLED.parse_sms(ret)

                        
            
                