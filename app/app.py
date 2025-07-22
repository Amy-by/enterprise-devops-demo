from flask import Flask, request
import time
import os

app = Flask(__name__)
REQUEST_COUNT = 0  # 记录请求次数（用于监控指标）

@app.route('/health')
def health():
    return {"status": "healthy"}, 200

@app.route('/metrics')  # 供Prometheus抓取的监控端点
def metrics():
    global REQUEST_COUNT
    REQUEST_COUNT += 1
    return {
        "request_count": REQUEST_COUNT,
        "uptime": time.time() - app.start_time,
        "version": os.getenv("APP_VERSION", "1.0.0")
    }, 200

@app.route('/delay')  # 模拟延迟接口（用于测试性能）
def delay():
    delay_time = request.args.get('time', 1, type=int)
    time.sleep(delay_time)
    return {"message": f"Slept for {delay_time} seconds"}, 200

if __name__ == '__main__':
    app.start_time = time.time()
    app.run(host='0.0.0.0', port=5000)
# 添加一行注释，触发流水线
