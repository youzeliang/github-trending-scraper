# GitHub 热门项目介绍（前50个）

## 1. yichuan-w/LEANN
LEANN是一个隐私优先的轻量级向量数据库,专为高效RAG应用设计,能将6000万文本块索引压缩至仅6GB存储空间,相比传统方案节省97%存储。支持本地运行,数据保持私密,可索引邮件、文档、聊天记录、代码库等多种个人数据源。采用图结构按需重计算机制,支持多种LLM提供商(OpenAI、Ollama、HuggingFace等),非常适合构建隐私安全的个人AI助手。

## 2. justlovemaki/AIClient-2-API
这是一个Node.js代理服务,统一多个大语言模型API的访问接口,支持Gemini CLI、Antigravity、Qwen Code、Kiro等模型。提供OpenAI兼容接口,使受限客户端模型(如Google Gemini、Claude)可通过标准API访问。具备账户池管理、智能故障转移、Web UI实时配置等功能,支持每日数千次免费请求,可与Cherry-Studio、NextChat、Cline等工具无缝集成,大幅降低API使用成本。

## 3. agrinman/tunnelto
用Rust编写的高性能工具,可将本地Web服务器通过公共URL暴露到互联网。支持自定义子域名、HTTPS、API密钥认证,提供通过Docker自建服务器的选项。安装简便(支持Homebrew、Cargo),使用异步IO和Tokio实现高效网络通信。采用gossip协议实现分布式部署,可在Fly.io全球多区域运行,是ngrok的开源替代方案。

## 4. jaywcjlove/awesome-mac
这是一个精心策划的Mac软件合集,收录了各类优质macOS应用程序,涵盖开发工具、设计产品、阅读写作、系统管理等多个类别。项目提供详细的软件分类、开源/免费标识、App Store链接,是Mac用户寻找优质软件的宝贵资源。拥有超过4万颗星,持续更新维护,社区活跃贡献,成为Mac软件推荐的权威列表。

## 5. metabase/metabase
Metabase是一款易用的开源商业智能(BI)和嵌入式分析工具,让团队成员无需SQL知识即可提问、创建仪表板和分析数据。支持高级SQL查询、交互式仪表板、告警和嵌入功能。拥有超过4.1万颗星,采用Clojure、TypeScript开发,支持自托管和云部署。提供丰富的文档、国际化支持和贡献指南,适合各类规模的组织使用。

## 6. cocoindex-io/cocoindex
CocoIndex是专为AI应用设计的数据转换框架,核心引擎用Rust编写以确保高性能,提供Python接口便于使用。支持开箱即用的增量处理和数据血缘追踪,可用约100行Python代码构建向量索引、知识图谱等复杂数据处理。强调开发速度、数据新鲜度和可观测性,兼容Postgres、Qdrant、LanceDB等多种存储方案,拥有活跃社区和详尽文档。

## 7. sgl-project/mini-sglang
Mini-SGLang是一个轻量级高性能LLM推理框架,用约5000行Python代码实现。旨在简化现代LLM服务系统的复杂性,提供透明模块化的代码库。采用radix缓存、分块预填充、重叠调度、张量并行等优化技术,支持多GPU设置。提供简单API用于在线服务、交互式shell和基准测试,兼容Qwen、Llama等主流模型,适合研究人员和开发者学习和部署LLM推理系统。

## 8. refly-ai/refly
Refly是首个开源的agent skills构建器,通过vibe workflow定义技能,可在Claude Code、Cursor、Codex等平台运行。采用可视化驱动的技能构建方式,提供有状态的可干预运行时,支持暂停、审计、中途纠正工作流。技能可导出为API、Webhook(Slack/Lark/Feishu)或集成到agent框架。提供中央技能注册表用于版本控制、分享和企业治理,集成超过3000个工具(Stripe、Salesforce、GitHub等)。

## 9. tursodatabase/turso
Turso是用Rust编写的进程内SQL数据库,与SQLite兼容,支持实时CDC、多语言SDK(Rust、Go、JavaScript、Python、Java)、异步IO、跨平台运行、向量搜索等功能。提供管理平台可创建和管理数十万个数据库,支持复制到任何位置(包括个人服务器),实现微秒级延迟访问。内置MCP服务器模式,可与AI助手和工具通过JSON-RPC交互,支持模式变更、查询和数据操作。

## 10. datawhalechina/hello-agents
这是一个从零开始构建智能体的中文开源教程,拥有超过2.1万颗星。系统讲解agent概念、历史、核心范式,提供ReAct、Plan-and-Solve、Reflection等经典框架的实践指南。包含Coze、Dify、n8n等低代码平台教程,以及从零构建自定义agent框架的分步指导。涵盖记忆系统、上下文工程、通信协议、agent训练(Agentic RL)等高级主题,提供智能旅行助手、自动研究agent、社会模拟环境等实战项目。

## 11. facebookresearch/sam3
SAM 3是Meta开发的统一基础模型,用于图像和视频的可提示分割,能使用文本、点、框、mask等多种提示检测、分割和跟踪对象。支持开放词汇表分割,处理超过27万个概念。提供预训练模型检查点、示例notebook,展示图像和视频分割用法。采用presence token架构改善相似提示的区分,通过解耦的检测器-追踪器设计实现高效扩展。拥有超过800万颗星,是计算机视觉领域的重要工具。

## 12. agentsmd/agents.md
AGENTS.md是一个简单开放的格式标准,用于指导AI编程agent。它类似于专门为AI agent设计的README,提供清晰的上下文和指令帮助AI agent有效地处理项目。格式简洁易采用,包含开发技巧、测试流程、PR指南等示例。由Agentic AI Foundation维护,被超过6万个GitHub仓库采用,兼容Codex、Copilot、Claude、Cursor等多种AI编程工具,是厂商中立的社区驱动标准。

## 13. trustedsec/social-engineer-toolkit
SET(Social-Engineer Toolkit)是TrustedSec开发的流行开源渗透测试框架,专为社会工程学攻击设计。提供各种自定义攻击向量模拟真实场景,主要用Python编写,兼容Linux和Mac OS X。拥有超过1.18万颗星,社区活跃贡献,提供详细安装和使用说明。仅供授权测试和教育目的使用,禁止用于非法活动。

## 14. trimstray/the-book-of-secret-knowledge
这是一个精心策划的资源集合,包含手册、备忘单、博客、hack技巧、单行命令、CLI/Web工具等,涵盖Linux、安全、DevOps、黑客等技术领域。拥有超过16.7万颗星,面向系统管理员、DevOps工程师、渗透测试人员和安全研究人员。内容组织清晰,提供shell单行命令、终端工具、网络工具等多个章节,是技术专业人士的宝贵知识库。

## 15. ZJU-LLMs/Foundations-of-LLMs
这是浙江大学DAILY实验室开发的大语言模型基础教材,系统讲解LLM相关知识。涵盖传统语言模型、LLM架构演进、提示工程、参数高效微调、模型编辑、检索增强生成等核心主题。设计注重易懂性、严谨性和深度,提供每月更新、相关论文、章节PDF等补充资源。还包含名为Agent-Kernel的新型多agent开发框架。拥有超过1.56万颗星,是学习和研究LLM的优质资源。

## 16. anthropics/skills
这是Anthropic的官方Agent Skills公开仓库,包含各种自包含技能,教Claude执行特定任务如文档创建、数据分析、创意艺术、企业工作流等。拥有超过7.5万颗星,主要用Python编写。技能可通过Claude平台(Claude.ai)、Claude Code插件或Claude API直接使用。提供创建新技能的指南和简单模板格式,许多技能采用Apache 2.0开源许可。支持渐进式披露,按需加载技能内容,保持上下文窗口高效可扩展。

## 17. safety-research/bloom
Bloom是一个开源Python工具,用于自动化评估大语言模型的行为特征,如谄媚、自我保护、政治偏见等。与固定基准不同,Bloom的评估基于种子配置,允许生成多样化和可重现的测试场景。支持生成评估场景、运行模型对话、评分和分析响应、多阶段处理(理解、构思、展开、判断)、交互式模型测试和结果可视化。集成Weights & Biases用于大规模实验,提供CLI和Python API编程访问,支持通过YAML文件自定义配置。

## 18. xerrors/Yuxi-Know
Yuxi-Know是一个结合LightRAG知识库的知识图谱智能问答系统,基于Langgraph、VueJS、Flask、Neo4j构建。支持多种大模型平台(OpenAI、Ollama、vLLM、国内厂商)和推理模型(如DeepSeek-R1)。提供灵活的知识库管理,支持多种文档格式(PDF、TXT、MD)和通过Neo4j的知识图谱集成。具有Web和知识图谱检索、可视化功能,通过API密钥轻松配置。设计注重易部署和定制化,支持在线大模型和本地模型,提供基于Docker的环境设置。

## 19. apurvsinghgautam/robin
Robin是一个AI驱动的暗网OSINT调查工具,利用大语言模型(OpenAI、Claude、Gemini或本地模型)优化搜索查询、过滤暗网搜索引擎结果并生成综合调查摘要。采用模块化架构,支持多模型、CLI优先设计、Docker部署选项,可扩展自定义搜索引擎和输出格式。需要Tor进行暗网搜索,支持多种部署方法(Docker、CLI二进制、Python开发)。拥有超过3500颗星,强调合法和教育用途,适合安全研究人员和威胁分析师。

## 20. ostris/ai-toolkit
AI-toolkit是微调扩散模型的终极训练工具包,支持在消费级硬件上训练和微调各种扩散模型(包括图像和视频模型)。提供GUI和CLI界面,强调易用性同时提供全面功能。支持最新扩散模型、至少24GB VRAM的GPU训练、集成Web UI用于管理训练任务、监控和模型发布、LoRA和LoKr等高级训练技术、云平台(RunPod、Modal)兼容性。拥有超过9100颗星,活跃维护,提供详尽文档和教程,采用MIT许可。

## 22. Shubhamsaboo/awesome-llm-apps
这是一个精心策划的大语言模型应用集合,包含使用OpenAI、Anthropic、Gemini和开源模型(Llama、DeepSeek、Qwen)构建的AI agents和RAG应用。拥有超过3万颗星,按入门和高级AI agents、多agent团队、语音AI agents、RAG系统等分类。推广开源AI Agent Hackathon,鼓励社区贡献。旨在展示跨研究、医疗、金融、游戏等领域的实用、创意和文档完善的LLM应用,为开发者提供资源和教程。

## 23. NanmiCoder/MediaCrawler
MediaCrawler是一个全面的网络爬虫项目,专注于从中国社交媒体和内容平台提取数据。支持小红书、抖音、快手、B站、微博、百度贴吧、知乎等平台。可进行关键词搜索、帖子详情检索、评论爬取(含二级评论)、用户资料爬取、评论词云生成。利用Playwright维护登录浏览器上下文并执行JavaScript获取加密参数,简化逆向工程过程。支持保存数据到数据库(MySQL)、CSV和JSON格式。拥有超过2.2万颗星,强调学习和研究用途,提供商业版本MediaCrawlerPro。

## 24. google-gemini/computer-use-preview
这是一个基于Python的工具,通过浏览器自动化agent模拟和预览计算机使用。支持本地使用Playwright运行或通过Browserbase远程运行,集成Google的Gemini API或Vertex AI用于语言建模。可基于自然语言查询自动化浏览器交互,适用于测试、演示或自动化工作流。提供详细的设置说明、API密钥配置、模型选择(默认gemini-2.5-computer-use-preview-10-2025),支持初始URL、调试选项等配置。有已知问题及解决方案,适合对AI驱动浏览器自动化感兴趣的开发者。

## 25. nocodb/nocodb
NocoDB是一个开源的自托管平台,作为Airtable的强大替代方案,通过类似电子表格的用户界面构建和管理数据库。主要用TypeScript开发,支持多种视图类型(网格、画廊、表单、看板、日历)、细粒度访问控制、与Slack、邮件服务、存储提供商的自动化集成。拥有超过6.2万颗星,活跃维护,频繁发布。提供Docker、各操作系统二进制文件、自动安装脚本等多种安装选项。旨在让数据库访问民主化,赋能互联网企业和个人用户开发强大的无代码数据库解决方案。

## 27. GitHubDaily/GitHubDaily
GitHubDaily是一个专注于分享高质量、有趣实用的开源技术项目的仓库。自2018年成立以来已累计分享超过1万个开源项目,内容涵盖人工智能、算法与数据结构、开发者工具、前后端开发、云原生、编程语言、资料集合、内容创作、媒体工具等多个技术领域。拥有超过4.5万颗星,社区活跃。旨在帮助开发者发现最新最火的开源项目,掌握前沿技术动态,扩大技术视野,通过源码阅读、学习和实践提升编程能力。还在微信公众号、微博、知乎、Twitter等多个平台传播优质开源内容。

## 28. livekit/agents
这是一个用于构建实时语音AI agents的强大开源框架,主要用Python实现。使开发者能够创建agent可以看、听、说的交互式应用,支持广泛的集成:语音转文本(STT)、大语言模型(LLM)、文本转语音(TTS)和实时通信API。提供作业调度、广泛的WebRTC客户端支持、电话集成、数据交换能力、语义转折检测等功能以增强对话流畅度。包含简单语音agent、多agent交接、背景音频、电话通话、结构化输出等示例,适合在实时环境中开发复杂的语音AI应用。

## 29. shareAI-lab/learn-claude-code
这是一个教育项目,专注于从零构建类似Claude Code的最小教育agent。用TypeScript和Python实现简单模块化的agent循环,设计用于教授AI agent开发的核心概念。通过12个渐进式学习课程,添加规划、上下文隔离、异步处理、团队协调、任务管理等机制。为教育目的简化,省略复杂的生产功能如事件总线、权限工作流和完整生命周期控制。提供克隆仓库、安装依赖、运行不同agent脚本的命令,以及用于可视化和文档的Web平台。

## 31. Lissy93/web-check
web-check是一个一体化开源OSINT工具,用于全面的网站分析,收集网站基础设施、安全和技术栈的详细见解。功能包括:网站基础设施分析(IP信息、服务器位置、DNS记录、开放端口、traceroute、关联主机名、重定向链、服务器详情);安全与隐私检查(SSL证书详情、HTTP头、security.txt、安全功能如HSTS、WAF检测、TLS配置、恶意软件/钓鱼列表检查);技术与内容见解(技术栈检测、网站地图解析、社交标签、cookie、链接页面、网站性能指标);域名与注册数据(Whois记录、DNSSEC、TXT记录、域名信息、邮件配置协议)。高度可定制,可通过多种方式部署,拥有超过1.95万颗星,活跃维护,鼓励社区贡献。

## 33. anthropics/claude-code-action
这是一个多功能GitHub Action,将Claude AI集成到开发工作流中。在拉取请求和issues内实现自动代码审查、回答问题和实施代码变更。根据上下文智能检测何时激活,支持代码分析、重构和自动化任务等功能,与GitHub评论和PR审查无缝集成。主要功能包括:无需额外配置的自动模式检测、交互式AI辅助、自动代码审查和建议、修复实施和新功能开发、进度跟踪和结构化JSON输出、兼容多个云提供商。用TypeScript编写,拥有超过5800颗星,提供详细设置指南、迁移说明和用例示例,适合寻求在GitHub中利用AI提升代码质量和工作流增强的团队。

## 35. marcelscruz/public-apis
这是一个协作式公共API列表,为开发者提供全面资源,托管在GitHub上拥有超过8195颗星。涵盖广泛主题和类别:动物、动漫、恶意软件、艺术与设计、认证、区块链、书籍、商业、日历、云存储、CI/CD、加密货币、货币兑换、数据验证、开发工具、词典、文档、健康、工作、机器学习、音乐、新闻、开放数据、开源项目、专利、性格、电话、摄影、播客、编程、科学与数学、安全、购物、社交媒体、体育与健身、测试、文本分析、跟踪、交通、URL缩短器、车辆信息、视频、天气等。活跃维护,拥有庞大的贡献者社区,每个API都标注了认证方法、HTTPS支持和CORS策略,为开发者寻求集成、实验或项目开发的公共API提供了宝贵资源。

## 36. kirodotdev/Kiro
Kiro是一个智能IDE,在软件开发生命周期(从原型到生产)中与开发者协作。利用AI驱动的功能:结构化规范、智能钩子、自然语言编程辅助、可自定义的项目指导,简化开发工作流。支持macOS、Windows和Linux多个平台。强调安全和隐私,提供全面文档、通过Discord的社区支持、通过MCP服务器集成外部工具的选项。旨在通过结合AI驱动自动化、项目特定规则和现代IDE环境中的对话式界面来提升生产力,拥有超过3000颗星,活跃开发和维护。

## 38. VectifyAI/PageIndex
PageIndex是VectifyAI开发的基于推理的无向量RAG创新系统,采用类人方式。不同于依赖语义相似性和分块的传统向量检索方法,PageIndex从长文档构建层次树结构,使LLM能够执行推理驱动、上下文感知的搜索。主要功能:不使用向量数据库或分块、类似详细目录的层次树索引、基于推理的类人可解释检索过程、在金融文档基准上的卓越准确率(98.7%)。用例包括分析冗长专业文档(财务报告、法律手册、学术文本),特别是传统向量搜索不足的领域。部署选项包括自托管、通过聊天平台的云服务或企业本地解决方案。开源代码、教程、cookbook和API集成,在财务文档QA基准中展示最先进结果,优于基于向量的方法。

## 40. ChromeDevTools/chrome-devtools-mcp
chrome-devtools-mcp是一个基于TypeScript的项目,提供Model-Context-Protocol(MCP)服务器,使AI编程agent(如Gemini、Claude、Copilot)能够控制和检查实时Chrome浏览器。通过Chrome DevTools和Puppeteer提供高级调试、性能分析和自动化功能。主要功能:性能洞察、网络分析、截图、控制台检查、可靠的自动化。支持多个MCP客户端集成,主要使用npx chrome-devtools-mcp@latest。要求Node.js v20.19+、Chrome(最新稳定版或更新)和npm。支持众多配置选项如连接现有Chrome实例、无头模式、自定义Chrome路径、类别(性能、网络、模拟)。提供多平台支持,包括与AMP、Antigravity、Claude、Cline、Codex、Copilot、Gemini、JetBrains、Kiro等工具的集成指南。

## 42. patchy631/ai-engineering-hub
AI工程中心是一个综合性资源库,汇集AI工程的最佳实践、工具、框架和教程。为AI工程师提供从入门到高级的完整学习路径和项目实践指南。

## 45. MiroMindAI/MiroThinker
MiroThinker是一个AI思考和推理框架,模拟人类思维过程进行复杂问题解决。采用多步推理和思维链技术,帮助AI系统做出更深入的分析和决策。

## 48. xpipe-io/xpipe
XPipe是一个连接管理器,用于管理和访问远程系统、容器、虚拟机等。提供统一界面管理SSH、Docker、Kubernetes等多种连接类型,支持文件传输、命令执行和终端访问。


**查询时间**: 2026年2月26日  
**数据来源**: 通过联网查询GitHub项目信息汇总整理  
**说明**: 每个项目用3句话概括其主要功能和特点
