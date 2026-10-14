# b2b-site-build-and-optimization (外贸 B2B 独立站建站与深度优化全案 Skill)

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![GitHub Repository](https://img.shields.io/badge/GitHub-cnproduct%2Fb2b--site--build--and--optimization-brightgreen)](https://github.com/cnproduct/b2b-site-build-and-optimization)
[![Sync Target](https://img.shields.io/badge/LAN%20Share-%5C%5Cnaike%5C耐科公司共享文件%5CAi学习%5CSkill-orange)](file://///naike/耐科公司共享文件/Ai学习/Skill)

> **外贸 B2B 独立站全生命周期建站与深度优化全案技能**  
> 沉淀自耐科礼品（Naike Gifts / Naike Group）出海独立站从 0 到 1 架构设计、工业证据化攻防、DVI 爆款商业情报穿透、交互式 CBM 集装箱海运计算器、$49.90 极速合规样品盒高转化漏斗，以及机器可读 GEO/AI 端点部署与全量自动回归的工程实战经验。

---

## 🎯 核心业务价值

1. **破除传统花架子，直击欧美采购审查心智**:
   - 传统建站堆砌口号；本方案通过 **>15kgf (149N) 实测破坏拉力**、一体注塑防脱扣工艺，超 ASTM F963-17 门槛 300%，直击 Amazon 42% 掉扣差评。
2. **商业情报与 DVI 套利落地**:
   - 实时嫁接 TikTok 115 亿播放量（如 Stanley 水杯吸管防尘帽）与 Temu/Shein 爆款，为海外采购商提供高溢价、零模具费出海矩阵。
3. **CBM 集装箱海运经济学计算器**:
   - 原生交互算清装箱率，以 40HQ 满载摊薄单件运费仅 $0.0022（1.6分钱人民币）极度震撼大买家，彻底破除“运费太贵”抗拒。
4. **$49.90 极速合规样品盒 (Master Swag Box)**:
   - 48 小时顺丰/DHL 空运直达，首单大货 $1,000 全额返还抵扣，一键表单预填，询盘转化率倍增。
5. **AI 搜索与 GEO 友好端点**:
   - 部署标准 `/llms.txt`、`/llms-full.txt`、`/ai/sku-matrix.json`、`/ai/compliance.json` 与 Schema.org 组织母集团架构，让 ChatGPT Search、Perplexity、Claude 优先收录并精准引述。

---

## 📂 仓库结构

```text
b2b-site-build-and-optimization/
├── SKILL.md                  # 核心技能指南与 9 大作战阶段标准 SOP
├── manifest.json             # 技能元数据与分类声明
├── README.md                 # 仓库与项目说明
├── LICENSE                   # MIT 开源协议
├── .gitignore                # 忽略配置文件
├── references/               # 标准模板与机器可读参考规范
│   ├── sku-matrix-template.json        # 机器可读 SKU 矩阵数据端点模板
│   ├── compliance-template.json       # 国际第三方实验室报告合规架构模板
│   ├── llms-template.txt              # LLM/AI 搜索抓取索引模板
│   └── schema-organization-template.json # 企业与母集团结构化标记范本
├── templates/                # 工业级响应式与交互组件源码
│   ├── footer-component.html          # 四列自适应证据链页脚组件
│   └── cbm-calculator-component.html  # 交互式集装箱海运计算器组件
└── scripts/                  # 自动化计算与运维同步脚本
    ├── cbm_calculator.py              # CBM 与装箱海运摊薄计算逻辑
    ├── deploy_and_verify.py           # 自动化部署与多断点验收脚本
    └── sync_skill.py                  # 多端自动化同步脚本 (GitHub + 局域网共享盘)
```

---

## 🔄 自动化多端同步机制 (Auto-Sync)

为保证团队协作与代码持续沉淀，本项目提供全自动化同步管道：

### 同步目标
1. **GitHub 远程组织仓库**: `https://github.com/cnproduct/b2b-site-build-and-optimization.git`
2. **耐科局域网共享盘**: `\\naike\耐科公司共享文件\Ai学习\Skill\b2b-site-build-and-optimization\`

### 触发方式
在任何一次网站更新、新增产品或参数优化后，只需执行以下命令：

```powershell
python scripts/sync_skill.py
```

脚本将自动完成：
1. 校验当前 Skill 目录的所有变更；
2. 自动在 GitHub `cnproduct` 组织下创建或更新仓库并 `git push`；
3. 镜像覆盖同步到公司局域网共享路径 `\\naike\耐科公司共享文件\Ai学习\Skill`；
4. 输出同步状态报告。

---

## 🤝 贡献与归属
- **Author**: cnproduct (RenWork AI Innovation Team)
- **Affiliation**: Naike Gifts / Naike Group
