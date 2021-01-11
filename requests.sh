#!bin/bash
#create
printf "[POST] - /api/v1/inventory \n"
curl -d '{"value":"86900012550","monthyPrice":15,"currency":"R$","setupPrice":25}' -H "Content-Type: application/json" http://web:5000/api/v1/inventory/
printf "\n"
#list
printf "[GET] - /api/v1/inventory \n"
curl -H "Content-Type: application/json" http://web:5000/api/v1/inventory/
printf "\n"
#update
printf "[PUT] - /api/v1/inventory/1 \n"
curl -X PUT -d '{"value":"8690001233","monthyPrice":15,"currency":"R$","setupPrice":25}'  -H "Content-Type: application/json" http://web:5000/api/v1/inventory/1
printf "\n"
#delete
printf "[DELETE] - /api/v1/inventory/1 \n"
curl -X DELETE -H "Content-Type: application/json" http://web:5000/api/v1/inventory/1
printf "\n"