# 常用命令
* bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 3 --partitions 2  --topic ktest01 (创建topic)

* bin/kafka-topics.sh --zookeeper localhost:2181 --list (列出所有topic)

* bin/kafka-console-producer.sh --broker-list localhost:9092 --topic ktest01 (生产消息)

* bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic ktest01 --from-beginning(消费消息)

* bin/kafka-topics.sh --describe --topic ktest01 --zookeeper localhost:2181 (查看topic详情)

* bin/kafka-topics.sh --zookeeper localhost:2181 --delete --topic ktest01 (删除topic)

* bin/kafka-consumer-groups.sh --bootstrap-server localhost:9092 --list(查看消费者组)

* bin/kafka-consumer-groups.sh --bootstrap-server localhost:9092  --describe --group console-consumer-13733 (查看消费者组的详情)
* ![[0880c08b0110c3da9612.png]]
* 生产的配置
* 
