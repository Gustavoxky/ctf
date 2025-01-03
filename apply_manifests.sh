#!/bin/bash

# Diretório dos manifestos
KUBERNETES_DIR="/home/gustavo/ctf/kubernetes"

# Verifique se o diretório existe
if [ ! -d "$KUBERNETES_DIR" ]; then
  echo "Erro: O diretório $KUBERNETES_DIR não existe."
  exit 1
fi

# Aplicar os manifestos Kubernetes
echo "Aplicando os manifestos Kubernetes..."
cd "$KUBERNETES_DIR" || exit

kubectl apply -f ctf-easy.yaml
kubectl apply -f ctf-medium.yaml
kubectl apply -f ctf-advanced.yaml
kubectl apply -f ctf-xss.yaml
kubectl apply -f ctf-deserialization.yaml
kubectl apply -f ctf-buffer_overflow.yaml
kubectl apply -f ctf-intermediate.yaml
kubectl apply -f ctf-expert.yaml
kubectl apply -f ctf-elite.yaml
kubectl apply -f ctf-legendary.yaml
kubectl apply -f ctf-mythical.yaml

echo "Todos os manifestos foram aplicados com sucesso!"
