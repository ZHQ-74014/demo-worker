# demo-worker

多仓全栈演示的 Python Worker 基线项目。

当前版本提供一个零依赖的 CSV 报表生成器，但还没有接入 API。后续 LoopForge 需求会让 API 写入任务队列，并让 Worker 消费任务、更新状态和生成文件。

## 运行一次

```bash
python3 worker.py \
  --report-id report-001 \
  --report-name sales \
  --output-dir /tmp/demo-reports
```

## 测试

```bash
python3 -m unittest discover -s tests -v
```

当前代码只使用 Python 标准库，不需要安装第三方依赖。
