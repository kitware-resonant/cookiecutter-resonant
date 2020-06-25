FROM minio/minio:latest AS builder
ARG MINIO_BACKEND_DIR
ARG MINIO_USER_ACCESS_KEY
ARG MINIO_USER_SECRET_KEY
# Install MinIO Client (mc)
RUN \
  wget https://dl.min.io/client/mc/release/linux-amd64/mc && \
  chmod +x mc
# Set admin credentials only during this build; these do not persist
ENV MINIO_ACCESS_KEY minioAdminAccess
ENV MINIO_SECRET_KEY minioAdminSecret
# * Start the MinIO server in the background
# * Wait for it bo be ready
# * Connect MinIO Client to the running MinIO server
# * Use MinIO Client to add an ordinary user
# * Use MinIO Client to grant the user read-write access to resources on the server
RUN \
  nohup sh -c "/usr/bin/docker-entrypoint.sh minio server ${MINIO_BACKEND_DIR} &" && \
  until nc -z localhost 9000; do sleep 1; done && \
  ./mc config host add minio http://localhost:9000 minioAdminAccess minioAdminSecret && \
  ./mc admin user add minio ${MINIO_USER_ACCESS_KEY} ${MINIO_USER_SECRET_KEY} && \
  ./mc admin policy set minio readwrite user=${MINIO_USER_ACCESS_KEY}

FROM minio/minio:latest
ARG MINIO_BACKEND_DIR
COPY --from=builder ${MINIO_BACKEND_DIR} ${MINIO_BACKEND_DIR}
