---
name: b2b-site-build-and-optimization
description: 外贸 B2B 独立站全生命周期建站与深度优化全案技能：从多页静态架构选型、工业证据化攻防（拉力测试>15kgf/ASTM合规闭环）、DVI爆款商业情报穿透、交互式CBM集装箱海运计算器、$49.90极速合规样品盒高转化漏斗，到机器可读GEO/AI端点 (llms.txt/sku-matrix.json)、Schema.org企业与母集团结构化标记、表单询盘闭环及Playwright全端视觉验收与多端持续同步机制。
---

# 外贸 B2B 独立站全生命周期建站与深度优化全案技能 (SOP)

> 本技能凝聚了耐科礼品（Naike Gifts / Naike Group）出海独立站从 0 到 1 架构搭建、工业证据化实证攻防、DVI 爆款商业情报落地、集装箱海运经济学交互计算、AI/GEO 机器可读端点部署，以及生产环境全量回归与自动化同步的实战工程经验。

---

## 目录
1. [核心定位与业务价值](#1-核心定位与业务价值)
2. [阶段一：高性能架构与响应式设计系统](#2-阶段一高性能架构与响应式设计系统)
3. [阶段二：工业证据化信任攻防体系](#3-阶段二工业证据化信任攻防体系)
4. [阶段三：跨品类爆款情报与 DVI 套利落地](#4-阶段三跨品类爆款情报与-dvi-套利落地)
5. [阶段四：交互式 CBM 集装箱海运计算器系统](#5-阶段四交互式-cbm-集装箱海运计算器系统)
6. [阶段五：$49.90 极速合规样品盒高转化漏斗](#6-阶段五4990-极速合规样品盒高转化漏斗)
7. [阶段六：机器可读 GEO 与 AI 搜索引擎友好端点](#7-阶段六机器可读-geo-与-ai-搜索引擎友好端点)
8. [阶段七：B2B 询盘捕获与表单邮件分发闭环](#8-阶段七b2b-询盘捕获与表单邮件分发闭环)
9. [阶段八：自动化多端视觉与功能回归验收规范](#9-阶段八自动化多端视觉与功能回归验收规范)
10. [阶段九：多端常态化自动同步与持续交付机制](#10-阶段九多端常态化自动同步与持续交付机制)

---

## 1. 核心定位与业务价值

### 1.1 破除外贸 B2B 建站传统误区
- **误区一：只看视觉，不看信任证据**。传统建站热衷于堆砌炫酷动画或假大空的口号，而欧美专业采购商（Procurement Managers）只关心核心痛点：质量是否稳定、拉力是否脱落、有无合规测试报告、工厂是否支持验厂。
- **误区二：重型框架滥用，牺牲速度与 SEO**。为了简单组件引入庞大的 SPA 框架，导致首屏水合延迟严重、搜索引擎蜘蛛与 AI 爬虫解析困难。
- **误区三：冷冰冰的产品目录，缺少商业情报赋能**。采购商不仅买产品，更需要买“能在他们本土市场爆卖的确定性”。

### 1.2 外贸采购决策委员会（Procurement Committee）四维审查心智模型
1. **合规安全 (Compliance & Safety)**: ASTM F963-17, EN71-1, California Prop 65, LFGB 权威实验室检测报告（SGS/TÜV/Intertek）。
2. **总持有成本 (TCO & Freight Efficiency)**: 不仅看出厂 FOB 价格，还要算清单箱装箱量、整柜（20GP/40HQ）摊薄后的单件到岸运费。
3. **交付敏捷度 (Sample & Lead Time Velocity)**: 能否 2-12 小时出 3D 渲染图？能否 48 小时发出真实样品盒？
4. **确定性与无风险承诺 (Risk Reversal)**: $49.90 样品费是否 100% 抵扣大货款？是否有破坏性测试实录？

---

## 2. 阶段一：高性能架构与响应式设计系统

### 2.1 技术选型准则
- **架构方案**: 多页静态 HTML5 + 模块化 Vanilla ES6+ JavaScript + 极简响应式 CSS / Tailwind CSS。
- **性能红线**:
  - TTFB (Time to First Byte) < 200ms
  - LCP (Largest Contentful Paint) < 1.2s
  - 零外部阻塞 CDN 依赖，核心字体与轻量样式本地静态托管。

### 2.2 跨页面导航栏状态与二级下拉菜单防闪烁机制
- **踩坑实录**: 多子页面（如 Blog、Evidence、Products）切换时，导航栏高亮丢失、二级下拉菜单（Dropdown）在移动端点击冲突或在特定页面丢失模块。
- **标准解决规范**:
  1. 使用绝对/规范相对路径（以 `/` 开头或严格计算相对层级），统一导航模板组件；
  2. 针对下拉菜单采用 CSS `:hover` 与 JavaScript `pointerenter`/`pointerleave` 双冗余防抖（Debounce 150ms），移动端采用触控委托代理；
  3. 通过 `data-nav-active` 属性动态标记当前路由，避免硬编码高亮。

### 2.3 工业级响应式页脚与证据徽章网格系统
- **布局核心**: 采用 CSS Grid + Flexbox 复合弹性容器：
  ```css
  .footer-proof-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
    gap: 1.5rem;
    align-items: stretch;
  }
  @media (max-width: 768px) {
    .footer-proof-grid {
      grid-template-columns: 1fr;
    }
  }
  ```
- **证据徽章标准化**: 将 ISO 9001、BSCI、ASTM F963、LFGB、Prop 65 等合规徽章统一 SVG 矢量化，保持 1:1 等高排布，在 375px 手机端至 1440px 桌面端杜绝文字溢出与空隙错位。

---

## 3. 阶段二：工业证据化信任攻防体系

### 3.1 痛点逆向击穿：亚马逊 42% 掉扣差评解构
- **行业痛点挖掘**: 海外买家在鞋饰（Shoe Charms / Croc Charms）类目中最主要的退货与差评原因是“底扣容易脱落导致儿童误吞窒息风险”。
- **攻击型卖点转化**:
  - 推出 **Anti-Detachment Guarantee（防脱扣专利级工艺）**；
  - 采用 **一体注塑（One-Piece Integral Molding）** 与 **超声波高周波深层熔接（Ultrasonic Fusion Welding）**；
  - 宣传口号明确：*“No Cheap Glue, Zero Detachment Risk”*。

### 3.2 破坏性实测拉力指标标准
| 指标分类 | 国际法规门槛 (ASTM F963-17 / EN71-1) | 行业普遍胶水粘贴水平 | 耐科一体化工艺实测标准 | 优势系数 |
| :--- | :--- | :--- | :--- | :--- |
| **破坏性脱离拉力** | 15.0 lbf (67.0 N) | 4.0 ~ 8.0 kgf (39 ~ 78 N) | **≥15.0 kgf (147.1 N) [Empirical Mean: 15.8 kgf]** | **超出 ASTM F963-17 强制门槛 220%+** |
| **扣脚扭力测试** | 0.45 N·m 持续 10 秒 | 容易底扣打转脱落 | **> 0.95 N·m 零形变** | **耐用度提升 2.1 倍** |
| **跌落冲击测试** | 1.2 米水泥地面 5 次跌落 | 脆裂脱层 | **1.8 米高处连续跌落 10 次无裂纹** | **军工级耐摔表现** |

### 3.3 权威检测报告（PDF）索取与合规通道
- 页面嵌入显性“Request Lab Report (PDF)”交互入口；
- 设立第三方实验室授权编号验证（如 SGS Ref No. CANEC2401829101）；
- 支持买家免注册即时查看水印预览版，并可通过表单索取未脱敏原始盖章检测文件。

---


### 3.4 关键合规红线：儿童产品安全法规边界与责任界定 (Crucial Regulatory Notice)
> **警示与合规原则**：欧美采购商法务最忌讳将“单一零部件拉力测试合格”等同于“整件商品符合儿童玩具安全”。
1. **测试对象精准界定**:
   - $\ge 15.0 \text{ kgf} (147.1 \text{ N})$ 测试**仅针对底扣与 PVC 软胶之间的物理抗拉拔结合力 (Mechanical Pull-Off Retention)**，证明其在正常及可预见滥用下不脱扣。
2. **整件商品合规要求 (Finished Goods Compliance)**:
   - 依据美国 CPSIA / 16 CFR § 1500 / 1501 与欧盟玩具安全指令 2009/48/EC，整件儿童产品必须进行全项化学与物理检测：
     * 基材总铅含量 (Total Lead in Substrate < 100 ppm)
     * 8 项禁限邻苯二甲酸盐 (8P Phthalates < 1000 ppm)
     * 尖点利边物理测试 (Sharp Edges / Sharp Points)
     * 溯源追踪标签 (Mandatory Tracking Labels)
3. **工厂责任闭环**:
   - 工厂提供 100% 合规环保 ATBC-PVC 及食品级铂金硅胶原料检测报告（SGS 报告编号：`SGS-SH-CANEC24018291-01`）；
   - 主动协助采购商将最终组装成品送检至指定第三方实验室（SGS / TÜV / Intertek），出具出海清关与零售上架的全项儿童安全证书。

## 4. 阶段三：跨品类爆款情报与 DVI 套利落地

### 4.1 商业情报源输入
- 整合 TikTok Shop 爆款趋势（如 #StanleyCup 115 亿+ 播放量）、Amazon Movers & Shakers 飙升榜、Google Trends 突变词与海关提单。
- 识别终端消费级需求（如水杯吸管防尘帽、装饰挂链、减压陀螺钥匙扣）并迅速嫁接工厂供应链。

### 4.2 DVI (Dynamic Viral Index) 爆款量化模型
$$DVI = 0.35 \times V_s + 0.30 \times M_s + 0.20 \times R_m + 0.15 \times E_f$$
- $V_s$ (Viral Velocity): 社媒播放与搜索指数增速
- $M_s$ (Margin Spread): 终端零售价与工厂 FOB 价套利倍数（>8x 为极高）
- $R_m$ (Mold Readiness): 工厂现模可用度（100 分 = 零模具费）
- $E_f$ (Freight Efficiency): 体积重量比与集装箱装载效能

### 4.3 首页高周转 6 大出海爆品矩阵标准配置
1. **NK-SC-PRO01**: Custom PVC Shoe Charms (拉力 >15kgf 一体成型，ASTM/EN71，现模 2,000+ 款)
2. **NK-VIR-SC08**: Stanley 40oz Tumbler Straw Charm & Dangle Chain (LFGB 铂金级硅胶，出厂 $0.45 对比海外零售 $8.99，20x 套利空间)
3. **NK-KC-ZIN03**: Heavy-Duty 3D Zinc Alloy Carabiner Keychain (盐雾测试 96h，车标/品牌金属周边)
4. **NK-KC-SPN04**: Kinetic Fidget Spinner Keychain (EDC 减压爆款，双精密静音轴承，转速 >90s)
5. **NK-MG-3DR05**: Micro-Injection 3D Soft PVC Fridge Magnet (多层次微量射出工艺，Pantone 专色精准还原)
6. **NK-PL-MST07**: Acrylic Liquid Floating Keychain (超声波无缝封装，高透矿物油防冻防漏)

---

## 5. 阶段四：交互式 CBM 集装箱海运计算器系统

### 5.1 痛点与心智攻坚
欧美批发买家与品牌采购在询价时最顾虑的是“空运太贵、海运不知具体成本”。
在产品详情页嵌入**交互式 CBM 海运计算器**，支持实时输入定制数量，瞬间得出箱规、重量、体积，并计算 20GP 与 40HQ 满柜摊薄单件运费。

### 5.2 核心算法与数据模型
- **单件毛重**: 6.8 g
- **装箱规格**: 2,500 pcs / CTN
- **外箱尺寸**: 42 cm × 32 cm × 28 cm ($0.037632 \text{ m}^3$)
- **外箱毛重**: 18.0 kg (实重)，体积重约为 $7.5 \text{ kg}$
- **标准集装箱容量**:
  - 20GP: 有效容积 $28.0 \text{ m}^3$（可装约 744 箱 / 186 万件）
  - 40HQ: 有效容积 $68.0 \text{ m}^3$（可装约 1,807 箱 / 451.7 万件）
- **摊薄结果震撼力**:
  - 40HQ 满载整柜海运费约 $3,200 时，单件平摊海运费仅为 **$0.0022（约合人民币 1.6 分钱）**！

### 5.3 交互实现要点
- 使用原生 JS 监听 `input` 事件，限制输入范围（100 ~ 5,000,000 件）；
- 动态平滑更新 DOM 节点；
- 提供“一键填入该数量发起报价 (Apply Quantity to RFQ)”锚点跳转。

---

## 6. 阶段五：$49.90 极速合规样品盒高转化漏斗

### 6.1 策略：小额付费试样过滤机制
- **问题**: 免费寄样会吸引大量无采购意向的个人买家，耗费工厂样板与快递费；
- **破局**: 设立 **$49.90 Master Compliance & Craft Swag Box**；
- **承诺**:
  1. **48h 极速空运出库**（DHL/FedEx 全球 3-5 天直达）；
  2. **100% Refundable**：首单大货量满 $1,000 时，样品费 $49.90 在定金中全额返还抵扣。

### 6.2 样品盒标准配置
1. 一体化注塑防脱扣鞋饰实测试样件（含 >15kgf 测力标识）；
2. Stanley 40oz 水杯配件与铂金硅胶吸管帽实物样；
3. 锌合金电镀质感色板（哑枪灰、玫瑰金、古青铜、亮光铬）；
4. 真实物理 Pantone 专色硅胶对比色卡；
5. 盖章版 ASTM F963 / LFGB 合规测试证书快照卡。

### 6.3 交互联动规范
在页面中所有样品盒卡片加入 `data-sample-action="master-swag-box"` 触发器。点击后平滑滚动至 RFQ 询盘表单，并自动注入以下内容：
- Subject: `[Sample Order] Request $49.90 Master Compliance Swag Box`
- Quantity: `1 Sample Box (100% Refundable)`
- Comments: `Please arrange 48h express dispatch. Delivery address attached.`

---

## 7. 阶段六：机器可读 GEO 与 AI 搜索引擎友好端点

### 7.1 面向 AI 搜索的下一代端点体系
新一代大模型（ChatGPT Search、Perplexity、Google AI Overviews、Claude）优先从结构化纯文本与 JSON 端点抓取产品数据与合规事实。

### 7.2 端点规范与目录结构
1. **`/llms.txt`**: 简明索引，包含工厂基本概况、核心工艺标准、合规认证编号、主流产品列表及机器端点链接。
2. **`/llms-full.txt`**: 详尽完整知识库，收录 8 大主流 SKU 的 BOM 成本分析、出厂阶梯价格、HS 编码、外箱装箱参数及采购委员会 Top 10 问答。
3. **`/ai/sku-matrix.json`**: RESTful 规范的产品矩阵 JSON 端点，便于 AI Agent 直接读取结构化产品规格。
4. **`/ai/compliance.json`**: 合规报告与实验室编号的权威数据端点。

### 7.3 Schema.org 组织与母集团结构化标记规范
```json
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "@id": "https://www.naikegifts.com/#organization",
  "name": "Naike Gifts",
  "legalName": "Jinjiang Naike Gifts Co., Ltd.",
  "alternateName": ["Naike", "Naike Group", "Naike Gifts"],
  "foundingDate": "2008",
  "url": "https://www.naikegifts.com/",
  "parentOrganization": {
    "@type": "Organization",
    "name": "Naike Group",
    "url": "https://naikegroup.com/"
  }
}
```

---

## 8. 阶段七：B2B 询盘捕获与表单邮件分发闭环

### 8.1 询盘表单架构与交互状态机
- **状态 1 (Idle)**: 表单字段验证（Email 格式校验、必填字段提示）；
- **状态 2 (Submitting)**: 提交按钮禁用，显示转圈加载动画，阻止重复点击；
- **状态 3 (Success)**: 弹出成功模态框（“RFQ Received - Lead Time 2 Hours”），重置表单；
- **状态 4 (Error)**: 友好降级提示（展示备用商务邮箱与 WhatsApp 直连按钮）。

### 8.2 邮件路由分发实现方案
1. **托管型端点 (如 Formspree)**:
   - 表单 `action` 挂载 `https://formspree.io/f/{FORM_ID}`；
   - Formspree 后台绑定业务主管企业邮箱，开启 SPF/DKIM 白名单，杜绝垃圾邮件拦截；
2. **自动化 Webhook 转发 (Serverless / Cloudflare Worker / Python API)**:
   - 接收表单 POST 请求 -> 校验 Honeypot 反垃圾字段 -> 调用企业微信/飞书/钉钉群机器人 Webhook 同步推送到手机；
   - 通过 SMTP / Resend API 自动向外贸业务员分发询盘细节，并向买家发送专业的 `Auto-Reply Confirmation`。

### 8.3 自动化测试与系统探针规范 (邮件与通知精准判断机制)
- **核心原则**: 所有由开发团队、CI/CD 自动化流水线、Playwright E2E 探针发起的测试提交，**邮件主题末尾必须强制包含【测试】字样**（如 ` - 【测试】`），确保业务团队在收件箱与钉钉群中能 100% 精准识别，绝不混淆真实客户订单。
- **系统级自动识别与双向防护**:
  1. **自动特征识别**: 后端 API 针对测试邮箱（`@example.com`, `@test.com`, `probe@`）、显式参数（`is_test: true`）、或测试关键词进行自动判定；
  2. **邮件主题统一打标**: 判定为测试时，邮件主题强制后缀 ` - 【测试】`；
  3. **正文置顶免责警示**: 邮件正文顶部插入高亮安全警示框：`⚠️ 【注意：此邮件为系统自动化测试 / 链路探针，非真实客户询盘！请勿跟进回复】`；
  4. **钉钉通知防误报**: 钉钉消息标题与正文同样追加 `【测试】` 标识，提示业务员“自动化链路检测正常，无需跟进报价”；
  5. **探针数据清理闭环**: 自动化回归完成后，必须清理数据库中的测试探针记录，保持商业分析报表与 CRM 数据纯净。

---

## 9. 阶段八：自动化多端视觉与功能回归验收规范

### 9.1 四大断点 Playwright 响应式截图回归
| 视口分类 | 分辨率 (Width x Height) | 核心验收重点 |
| :--- | :--- | :--- |
| **Desktop** | 1440 × 900 | 导航栏下拉菜单展开、CBM 计算器双列布局、底栏对齐 |
| **Laptop** | 1200 × 800 | 1200px 断点栅格收缩、证据徽章居中无断行 |
| **Tablet** | 768 × 1024 | 导航栏汉堡按钮折叠、表格水平滚动提示、计算器单列切换 |
| **Mobile** | 375 × 812 | 底部 Sticky 询盘按钮、大拇指触控热区、表单全宽适配 |

### 9.2 自动化部署流（Zero-Downtime）
- 使用 SSH + rsync 将编译后或多页静态源文件同步到目标服务器；
- 采用版本目录软链接机制（`releases/YYYYMMDD_HHMMSS` -> `current`），发生异常时 1 秒软链接回滚；
- 部署后自动执行 `curl -I` 检查状态码 200，并抓取实时网页截图存档。

---

## 10. 阶段九：多端常态化自动同步与持续交付机制

### 10.1 同步目标
1. **GitHub 远程组织仓库**: `https://github.com/cnproduct/b2b-site-build-and-optimization.git`
2. **企业局域网共享目录**: `\\naike\耐科公司共享文件\Ai学习\Skill\b2b-site-build-and-optimization\`

### 10.2 自动化同步脚本 `sync_skill.py`
在技能的 `scripts/` 目录下提供自动化同步脚本，执行时：
1. 校验本地 Skill 完整性与各模块文件；
2. 自动检查并创建 GitHub 仓库（若未创建），执行 `git add`, `git commit`, `git push`；
3. 镜像复制最新内容到局域网共享目录，确保团队成员在 Windows 局域网即时同步。

### 10.3 持续联动工作流建议
后续对网站的每一次重大迭代（如新增产品线、优化 CBM 参数、新增合规认证）完成后：
- 运行：`python d:\自建站\.agents\skills\b2b-site-build-and-optimization\scripts\sync_skill.py`
- 即可一键完成 GitHub 和公司局域网共享文件的双重同步，形成企业沉淀。
