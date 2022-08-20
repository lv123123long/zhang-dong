# clickhouse增加全局线程池参数
## 配置文件clickhouse-config
### 配置项max_thread_pool_free_size
#### 新增
##### 1000
### thread_pool_queue_size
#### 新增
##### 4000


## 配置文件clickhouse-config
### 配置项clucene_search_cache_size
#### 删掉
### 配置项 fulltext_search_cache_size
#### 新增
##### 5368709120
## 配置文件clickhouse-config/merge_tree
### 配置项allow_use_index_internal_merge
#### 新增20220414
##### 1
* 默认关闭对sailfish merge优化
* 修改  0*
* 20220602
### 变更参数名称clucene_search_cache_size到fulltext_search_cache_size

# 优化merge_tree 中part写入相关参数
## 配置文件clickhouse-config/merge_tree
### 配置项 max_parts_in_total
#### 修改
##### 15000
### 配置项parts_to_throw_insert
#### 修改
##### 1300
### 配置项max_delay_to_insert
#### 修改
##### 5
### 配置项parts_to_delay_insert
#### 修改
##### 1000
## 配置文件clickhouse-users
## 优化alter 在ReplicatedMergeTree类型表执行时的失败问题
### 配置项replication_alter_partitions_sync
#### 修改
##### 1
## 优化明细查询在小数据量下，返回total不准的问题
### 配置项optimize_read_in_total
#### 新增
##### 1000





