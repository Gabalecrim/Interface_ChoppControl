from serial import *
import time
import asyncio

class espUtils:
    runing = False

    @staticmethod
    async def update_timer(self):
        while espUtils.runing:
            await asyncio.sleep(1)
            


    @staticmethod
    def read():
        obj = espUtils.Data
        if isinstance(obj,Serial):
            if(obj.in_waiting != 0):
                if (not obj.is_open):
                    obj.open()
                rec = obj.read_all()
                rec = rec.decode()
                return rec
        return "False"
        
    @staticmethod
    def sendReadValue(msg,wait=0.1):
        time.sleep(wait)
        espUtils.flushInput()#limpa serial
        espUtils.send(msg)
        time.sleep(wait)
        resul = espUtils.read()
        resulV = resul.split("\n")
        resulV = resulV[1].replace("\r","")
        return resulV
    @staticmethod
    def flushInput():
        espUtils.Data.reset_input_buffer()
    @staticmethod
    def send(msg,wait=0.1):
        obj = espUtils.Data
        if isinstance(obj,Serial):
            if (not obj.is_open):
                obj.open()
            obj.write((msg + "\r").encode())
            time.sleep(wait)
    @staticmethod
    def startSerial(COM,Baudrate,Timeout):
        espUtils.Data = Serial(COM, baudrate = Baudrate, timeout = Timeout)

class storage:
    SetPoint_de_fluxo = 0
    SetPoint_de_fluxo_baixo = 0
    Velocidade_servo_ms = 0
    Velocidade_do_servo_fim_de_envase_ms = 0
    Set_scale = 0
    Densidade = 0
    SetPoint_de_volume = 0
    Integral_PIGid = 0
