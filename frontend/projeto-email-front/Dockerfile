# Etapa de build
FROM node:20 AS builder

WORKDIR /app
COPY . .
RUN npm install
RUN npm run build

# Etapa de produção
FROM nginx:alpine
COPY --from=builder /app/dist /usr/share/nginx/html

# Copia config customizada opcional (não obrigatório)
# COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80
