# 构建阶段：安装依赖
FROM python:3.9-slim AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt  # 使用国内pip源加速

# 运行阶段：精简镜像
FROM python:3.9-alpine
WORKDIR /app
COPY --from=builder /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages
COPY app.py .
# 应用版本变量（注释单独成行，避免ENV指令语法错误）
ENV APP_VERSION=1.0.0
EXPOSE 5000
CMD ["python", "app.py"]
