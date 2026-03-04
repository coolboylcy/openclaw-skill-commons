# OpenClaw Skill Commons 快速入门教程

> 5 分钟开始使用 774+ OpenClaw 技能

## 🚀 第一步：安装 Skill Voter

```bash
npx clawhub@latest install skill-voter
```

## 📊 第二步：查看热门技能

```bash
# 查看 Top 10 技能
curl -s https://raw.githubusercontent.com/openclaw-commons/openclaw-skill-commons/main/leaderboard.json \
  | python3 -c "import json,sys; d=json.load(sys.stdin); [print(f'{i:2}. {s[\"name\"]:<28} score={s[\"score\"]:+.1f}') for i,s in enumerate(d['skills'][:10],1)]"
```

## 🔍 第三步：搜索技能

访问技能浏览器：https://openclaw-commons.github.io/openclaw-skill-commons/

- 使用搜索框查找技能
- 按分类筛选（Python/Node.js/DevOps等）
- 查看技能详情和安装命令

## 📦 第四步：安装技能

```bash
# 安装单个技能
npx clawhub@latest install weather
npx clawhub@latest install git-essentials
npx clawhub@latest install daily-briefing

# 批量安装（推荐）
npx clawhub@latest install weather git-essentials daily-briefing pomodoro
```

## 🗳️ 第五步：投票

使用技能后，根据体验投票：

```bash
# 好用 +1
python3 scripts/vote.py vote weather +1

# 不好用 -1
python3 scripts/vote.py vote bad-skill -1
```

## 📈 第六步：查看统计

访问网站查看实时统计：
- 技能总数：774+
- 今日投票数
- 活跃用户数
- 热门技能排行榜

## 💡 常用技能推荐

### 新手必装（10 个）

```bash
npx clawhub@latest install \
  weather \
  git-essentials \
  github \
  daily-briefing \
  habit-tracker \
  pomodoro \
  task-decomposer \
  brave-search \
  transcript \
  skill-creator
```

### Python 开发者（10 个）

```bash
npx clawhub@latest install \
  python-quickstart \
  pytest-testing \
  black-formatter \
  flask-boilerplate \
  django-starter \
  pandas-analysis \
  requests-http \
  beautifulsoup-scraping \
  sqlalchemy-orm \
  fastapi-guide
```

### DevOps 工程师（10 个）

```bash
npx clawhub@latest install \
  docker-essentials \
  kubernetes-basics \
  ci-cd-guide \
  terraform-basics \
  ansible-playbooks \
  prometheus-monitoring \
  grafana-dashboards \
  nginx-config \
  ssl-certificate \
  backup-strategy
```

## 🤝 贡献技能

发现缺少某个技能？自己创建一个！

```bash
# 使用 skill-creator 创建新技能
npx clawhub@latest install skill-creator
openclaw skill-creator --name my-awesome-skill
```

## 📚 更多资源

- **GitHub**: https://github.com/openclaw-commons/openclaw-skill-commons
- **网站**: https://openclaw-commons.github.io/openclaw-skill-commons/
- **文档**: SKILLS_BY_CATEGORY.md
- **投票协议**: PROTOCOL.md

## ❓ 常见问题

### Q: 技能安装失败？
A: 检查 clawhub 版本：`npx clawhub@latest --version`，升级到最新版

### Q: 如何更新技能？
A: `npx clawhub@latest update <skill-name>`

### Q: 投票后排行榜何时更新？
A: GitHub Actions 每小时自动更新 leaderboard.json

### Q: 如何联系社区？
A: 加入 Telegram 群组或 GitHub Discussions

---

**最后更新**: 2026-03-04
**维护者**: OpenClaw Community
