from flask import Flask, render_template, request, jsonify
# import paho.mqtt.publish as publish
import paho.mqtt.client as mqtt

app = Flask(__name__)

# 웹 페이지 라우트
@app.route('/')
def index():
    capacity = 75  # 예시 용량 값
    return render_template('test.html', capacity=capacity)

# MQTT 메시지 발행 함수
def publish_mqtt_message():
    client = mqtt.Client()
    client.connect("192.168.20.93", 1883, 60)
    client.publish("maple/word",'1')

# 쓰레기통 출발 처리 함수
@app.route('/start', methods=['POST'])
def start_trash():
    try:
        publish_mqtt_message()
        return jsonify({'message': '쓰레기통 출발이 요청되었습니다.'}), 200
    except Exception as e:
        return jsonify({'message': '쓰레기통 출발 요청을 실패했습니다.'}), 500

if __name__ == '__main__':
    app.run(debug=True)
