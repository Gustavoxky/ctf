#!/bin/bash

# Construir imagens para cada nível
docker build -t ctf-easy:latest ./easy
docker build -t ctf-medium:latest ./medium
docker build -t ctf-advanced:latest ./advanced
docker build -t ctf-xss:latest ./xss
docker build -t ctf-deserialization:latest ./deserialization
docker build -t ctf-buffer_overflow:latest ./buffer_overflow
docker build -t ctf-intermediate:latest ./IntermediateFileUploadVulnerability
docker build -t ctf-expert:latest ./ExpertSSRF
docker build -t ctf-elite:latest ./EliteRCE
docker build -t ctf-legendary:latest ./LegendaryAuthenticationBypass
docker build -t ctf-mythical:latest ./MythicalRaceCondition

echo "Todas as imagens foram construídas com sucesso!"
