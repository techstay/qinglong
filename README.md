# qinglong

自用青龙脚本仓库，包含了一些自己平时在用的脚本，使用详情参见各脚本注释。

- `glados_checkin`，glados 签到脚本，使用前需要在配置文件中添加自己的 cookie。
- `sockboom_checkin`，sockboom 签到脚本，使用之前需要设置 API key

## 开始使用

### 添加订阅

```sh
ql repo https://ghproxy.com/https://github.com/techstay/qinglong "glados_checkin" "" "notify.py" main
```

### 依赖

运行脚本需要安装一些依赖，可以在青龙面板的*依赖管理*处安装。

python 依赖

```txt
requests
python-dotenv
```
