# -*- coding: utf-8 -*-
"""
Author: niziheng
Created Date: 2021/9/20
Last Modified: 2021/9/20
Description: basic of pika.
"""

# 概念
# 1. Broker: 消息队列的服务器实体
# 2. Exchange: 消息交换机，指定消息进入队列的规则
# 3. Queue: 消息队列的载体，每个消息都被存入一个或者多个队列
# 4. Binding: 绑定规则，把Exchange和Queue按照路由规则绑定起来
# 5. Routing Key: 路由关键字，Exchange会根据这个key进行消息投放
# 6. vhost: 虚拟主机，一个broker中存放多个vhost，用于用于权限隔离
# 7. Producer: 生产者
# 8. Consumer: 消费者
# 9. Channel: 消息信道，客户端可以建立多个连接，每个连接又可建立多个信道(Channel)，每个信道代表一个回话任务



