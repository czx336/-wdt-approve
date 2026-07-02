name: WDT自动退货审批
on:
  schedule:
    - cron: '0 2 * * *'
  workflow_dispatch:

jobs:
  run_approve_task:
    runs-on: ubuntu-latest
    steps:
      - name: 拉取仓库代码
        uses: actions/checkout@v4

      - name: 配置Python环境
        uses: actions/setup-python@v5
        with:
          python-version: "3.11"

      - name: 安装依赖requests
        run: pip install requests

      - name: 执行审批脚本
        env:
          WDT_ACCOUNTS: ${{ secrets.WDT_ACCOUNTS }}
        run: python approve.py
