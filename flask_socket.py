from flask import Flask, render_template, request, jsonify
import paho.mqtt.client as mqtt

app = Flask(__name__)

# MQTT 클라이언트 생성
mqtt_client = mqtt.Client()


# MQTT 브로커에 연결하는 콜백 함수
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))


# MQTT 클라이언트에 콜백 함수 등록
mqtt_client.on_connect = on_connect

# MQTT 브로커에 연결
mqtt_broker_address = "broker.hivemq.com"
mqtt_port = 1883
mqtt_client.connect(mqtt_broker_address, mqtt_port, 60)

# MQTT 클라이언트 루프 실행
mqtt_client.loop_start()


# 웹 페이지 라우트
@app.route("/")
def index():
    capacity = 75  # 예시 용량 값
    return render_template("test.html", capacity=capacity)


# MQTT 메시지 발행 함수
def publish_mqtt_message():
    mqtt_client.publish("maple/world", "1")


# 쓰레기통 출발 처리 함수
@app.route("/start", methods=["POST"])
def start_trash():
    try:
        publish_mqtt_message()
        return jsonify({"message": "쓰레기통 출발이 요청되었습니다."}), 200
    except Exception as e:
        return jsonify({"message": "쓰레기통 출발 요청을 실패했습니다."}), 500


if __name__ == "__main__":
    app.run(host = '0.0.0.0', debug=True)