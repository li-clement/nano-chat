import threading
import sys
import nls
import os

URL="wss://nls-gateway.cn-shanghai.aliyuncs.com/ws/v1"
TOKEN="4cd8d0c1c4f14578b97d9c70e9577e9b"  #参考https://help.aliyun.com/document_detail/450255.html获取token
APPKEY="SU7lo0IdV2RiVif6"       #获取Appkey请前往控制台：https://nls-portal.console.aliyun.com/applist

class TestTts:
    def __init__(self, tid, test_file):
        self.__th = threading.Thread(target=self.__test_run)
        self.__id = tid
        self.__test_file = test_file
   
    def start(self, text):
        self.__text = text
        self.__f = open(self.__test_file, "wb")
        self.__th.start()
    
    def test_on_metainfo(self, message, *args):
        print("on_metainfo message=>{}".format(message))  

    def test_on_error(self, message, *args):
        print("on_error args=>{}".format(args))

    def test_on_close(self, *args):
        print("on_close: args=>{}".format(args))
        try:
            self.__f.close()
            print("play " + self.__f.name)
        except Exception as e:
            print("close file failed since:", e)

    def test_on_data(self, data, *args):
        try:
            self.__f.write(data)
        except Exception as e:
            print("write data failed:", e)

    def test_on_completed(self, message, *args):
        print("on_completed:args=>{} message=>{}".format(args, message))


    def __test_run(self):
        print("thread:{} start..".format(self.__id))
        tts = nls.NlsSpeechSynthesizer(
                    url=URL,
                    token=TOKEN,
                    appkey=APPKEY,
                    on_metainfo=self.test_on_metainfo,
                    on_data=self.test_on_data,
                    on_completed=self.test_on_completed,
                    on_error=self.test_on_error,
                    on_close=self.test_on_close,
                    callback_args=[self.__id]
                )

        print("{}: session start".format(self.__id))
        r = tts.start(self.__text,voice="ailun",aformat="wav", speech_rate=-200)#,aformat="wav"
        print("{}: tts done with result:{}".format(self.__id, r))

# def multiruntest():
#       name = "thread" #+ str(i)
#       t = TestTts(name, "1.wav")
#       t.start(TEXT)