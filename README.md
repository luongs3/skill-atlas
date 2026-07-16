# Skill Atlas

![Skill Atlas — a trust-rated index of public AI-agent skills, organized by job. Trust tiers A (canonical) to D (caution).](assets/hero.png)

**A curated, trust-rated index of public AI-agent skills, organized by job.**

This is not a skill store and not another dump of links. It answers one question an
agent (or a person configuring one) actually has:

> *"I'm about to do **X** (work on Upwork / run an interview / learn English).
> Which public skills should I load, and can I trust them?"*

The skills themselves live in their original repos. This atlas only catalogs **which
ones are good, where they come from, and how stale they are** — the trust layer that
every `awesome-*` list skips.

## Why this exists

A skill is *instructions an AI follows confidently*. That makes a stale or wrong skill
**worse than no skill** — it produces a confident wrong answer instead of making the
agent think. A public skill is only useful if you can answer three things about it
before loading:

1. **Source** — who wrote it, and is that source reputable? (verifiable identity, not a self-claim)
2. **Freshness** — when was it last validated against current tools? (a date someone re-checked, not the publish date)
3. **Fit** — what does it assume about your environment?

Every entry in this atlas carries that metadata. See [`_meta/SCHEMA.md`](_meta/SCHEMA.md).

## Install (use it as a skill)

The atlas ships as a loadable **Agent Skill**. Drop it where your agent looks for skills
so it reaches for the atlas automatically at the start of a task:

```bash
# Claude Code / Hermes-style skills dir (adjust path to your setup)
git clone https://github.com/luongs3/skill-atlas \
  ~/.claude/skills/skill-atlas
```

Once installed, your agent loads `skill-atlas` when a task matches a known job and pulls
the right trust-rated skills for it. No install needed to just browse — read [`jobs/`](jobs/) directly.

**Uninstall:** it's a single self-contained directory with no global state, hooks, or
background process — just delete it:

```bash
rm -rf ~/.claude/skills/skill-atlas
```

## How to use it

![How Skill Atlas works: task → route to job → vetted tiered skills (A/B/C/D) → fork it private.](assets/how-it-works.png)

1. Find your job under [`jobs/`](jobs/) (e.g. [`jobs/upwork.md`](jobs/upwork.md)).
2. Read the ranked skill list. Each entry has a **trust tier**, source URL, and last-validated date.
3. Load the public skill into your agent.
4. **Fork it private and adapt it to yourself.** The public skill is the starting
   point; your private version encodes your voice, creds, and rules. Never publish the
   private fork.

## Trust tiers (full definitions in `_meta/SCHEMA.md`)

| Tier | Meaning |
|------|---------|
| 🟢 **A — Canonical** | Official vendor source (Anthropic, the spec author). Trust by authorship. |
| 🔵 **B — Community-proven** | High reputation (stars/installs/maintainer track record) + actively maintained. |
| 🟡 **C — Useful, verify** | Plausible and useful but low/unknown reputation or unmaintained. Read before trusting. |
| 🔴 **D — Caution** | Stale, unmaintained >12mo, or known-broken against current tools. Listed so you don't rediscover it. |

## Index of jobs

_211 jobs, 594 skill entries — every GitHub source live-verified via `gh api` (2026-06-19 or newer). Tier shown is the lead tier; open a job for the full tiered list._

| Job | Best tier | File |
|-----|-----------|------|
| 3D Web Graphics | 🟢 A | [`3d-web-graphics.md`](jobs/3d-web-graphics.md) |
| Accountant / Bookkeeper | 🔵 B | [`accountant-bookkeeping.md`](jobs/accountant-bookkeeping.md) |
| Agent Frameworks — LangGraph, CrewAI, AutoGen | 🟢 A | [`agent-frameworks-langgraph.md`](jobs/agent-frameworks-langgraph.md) |
| AI Agent Orchestration | 🟢 A | [`ai-agent-orchestration.md`](jobs/ai-agent-orchestration.md) |
| Algorithms & System Design | 🔵 B | [`algorithms-system-design.md`](jobs/algorithms-system-design.md) |
| Analytics Engineering (dbt) | 🟢 A | [`dbt-analytics-engineering.md`](jobs/dbt-analytics-engineering.md) |
| Angular Development | 🟢 A | [`angular-development.md`](jobs/angular-development.md) |
| Ansible — Config Management & Automation | 🟢 A | [`ansible-automation.md`](jobs/ansible-automation.md) |
| Apache Airflow — Data Orchestration | 🟢 A | [`airflow-orchestration.md`](jobs/airflow-orchestration.md) |
| Apache Kafka — Event Streaming | 🟢 A | [`kafka-event-streaming.md`](jobs/kafka-event-streaming.md) |
| API Contract Testing | 🟢 A | [`contract-testing.md`](jobs/contract-testing.md) |
| API Design (REST & gRPC) | 🔵 B | [`api-design.md`](jobs/api-design.md) |
| API Mocking & Test Doubles | 🟢 A | [`mocking-test-doubles.md`](jobs/mocking-test-doubles.md) |
| App Search — Meilisearch & Typesense | 🟢 A | [`search-meilisearch-typesense.md`](jobs/search-meilisearch-typesense.md) |
| Application Security | 🟢 A | [`security.md`](jobs/security.md) |
| AR / VR / XR Development | 🟢 A | [`ar-vr-xr.md`](jobs/ar-vr-xr.md) |
| Astro — Content-First Sites | 🟢 A | [`astro-content-sites.md`](jobs/astro-content-sites.md) |
| Auth Providers — Keycloak, Auth.js, Authentik | 🟢 A | [`auth-providers.md`](jobs/auth-providers.md) |
| Authentication & Authorization | 🟢 A | [`authentication-authorization.md`](jobs/authentication-authorization.md) |
| Backend-as-a-Service | 🔵 B | [`backend-as-a-service.md`](jobs/backend-as-a-service.md) |
| Backup & File Sync | 🟢 A | [`backup-sync-tools.md`](jobs/backup-sync-tools.md) |
| Bevy (Rust Game Dev) | 🟢 A | [`bevy-rust-gamedev.md`](jobs/bevy-rust-gamedev.md) |
| Big Data Processing (Spark) | 🟢 A | [`spark-big-data.md`](jobs/spark-big-data.md) |
| Building Go CLIs | 🔵 B | [`go-cli-tools.md`](jobs/go-cli-tools.md) |
| Building MCP Servers & Agent Tools | 🟢 A | [`mcp-and-agent-tools.md`](jobs/mcp-and-agent-tools.md) |
| Building TUIs — Terminal UIs | 🟢 A | [`cli-tui-frameworks.md`](jobs/cli-tui-frameworks.md) |
| C# / .NET Development | 🟢 A | [`csharp-dotnet-development.md`](jobs/csharp-dotnet-development.md) |
| Career Roadmaps & CS Fundamentals | 🔵 B | [`career-roadmaps.md`](jobs/career-roadmaps.md) |
| Chaos Engineering | 🔵 B | [`chaos-engineering.md`](jobs/chaos-engineering.md) |
| CI/CD Pipelines | 🟢 A | [`cicd-pipelines.md`](jobs/cicd-pipelines.md) |
| Cilium & eBPF Networking | 🟢 A | [`cilium-ebpf-networking.md`](jobs/cilium-ebpf-networking.md) |
| Classical ML — scikit-learn & Boosting | 🟢 A | [`classical-ml-sklearn.md`](jobs/classical-ml-sklearn.md) |
| CLI Data Wrangling — CSV/JSON | 🟢 A | [`csv-data-wrangling.md`](jobs/csv-data-wrangling.md) |
| ClickHouse — OLAP & Analytics DB | 🟢 A | [`clickhouse-olap.md`](jobs/clickhouse-olap.md) |
| Cloud (AWS & GCP) | 🟢 A | [`cloud-aws-gcp.md`](jobs/cloud-aws-gcp.md) |
| Cloud Cost & FinOps | 🟢 A | [`cost-finops.md`](jobs/cost-finops.md) |
| Code Quality & Linting | 🟢 A | [`code-quality-linting.md`](jobs/code-quality-linting.md) |
| Columnar Data (Apache Arrow) | 🟢 A | [`apache-arrow-data.md`](jobs/apache-arrow-data.md) |
| Computer Vision (OpenCV) | 🟢 A | [`computer-vision-opencv.md`](jobs/computer-vision-opencv.md) |
| Consul — Service Discovery & Mesh | 🟢 A | [`consul-service-discovery.md`](jobs/consul-service-discovery.md) |
| Container & Supply-Chain Security | 🟢 A | [`container-image-scanning.md`](jobs/container-image-scanning.md) |
| Container Runtimes & Compose | 🟢 A | [`container-runtimes.md`](jobs/container-runtimes.md) |
| Crossplane — Control-Plane IaC | 🟢 A | [`crossplane-control-plane.md`](jobs/crossplane-control-plane.md) |
| Customer Support Agent / Support Ops | 🔵 B | [`customer-support-agent.md`](jobs/customer-support-agent.md) |
| Dagster & Prefect — Modern Pipelines | 🟢 A | [`dagster-prefect-pipelines.md`](jobs/dagster-prefect-pipelines.md) |
| Dart Language | 🟢 A | [`dart-language.md`](jobs/dart-language.md) |
| Data & Model Versioning | 🟢 A | [`data-versioning.md`](jobs/data-versioning.md) |
| Data Analysis | 🟢 A | [`data-analysis.md`](jobs/data-analysis.md) |
| Data Engineering | 🟢 A | [`data-engineering.md`](jobs/data-engineering.md) |
| Data Serialization & Query | 🟢 A | [`data-serialization-formats.md`](jobs/data-serialization-formats.md) |
| Data Validation & Quality | 🟢 A | [`data-validation-quality.md`](jobs/data-validation-quality.md) |
| Data Visualization | 🔵 B | [`data-visualization.md`](jobs/data-visualization.md) |
| Databases & SQL (PostgreSQL-first) | 🟢 A | [`databases-sql.md`](jobs/databases-sql.md) |
| dbt — SQL Transformations (deep) | 🟢 A | [`dbt-transformations.md`](jobs/dbt-transformations.md) |
| Desktop & GUI Automation | 🔵 B | [`automation-scripting-python.md`](jobs/automation-scripting-python.md) |
| DevOps & Infrastructure | 🟢 A | [`devops-infrastructure.md`](jobs/devops-infrastructure.md) |
| Diagrams as Code | 🟢 A | [`diagramming-as-code.md`](jobs/diagramming-as-code.md) |
| Distributed & Large-Model Training | 🟢 A | [`distributed-training.md`](jobs/distributed-training.md) |
| Distributed Databases | 🟢 A | [`distributed-databases.md`](jobs/distributed-databases.md) |
| Django Development | 🟢 A | [`django-development.md`](jobs/django-development.md) |
| Docker & Containers | 🟢 A | [`docker-containers.md`](jobs/docker-containers.md) |
| Dynamic Secrets & PKI (Vault deep) | 🟢 A | [`vault-dynamic-secrets.md`](jobs/vault-dynamic-secrets.md) |
| Elasticsearch — Search & Analytics | 🟢 A | [`elasticsearch-search.md`](jobs/elasticsearch-search.md) |
| Electron & Tauri — Desktop Apps | 🟢 A | [`electron-desktop-apps.md`](jobs/electron-desktop-apps.md) |
| Elixir & Phoenix | 🟢 A | [`elixir-phoenix.md`](jobs/elixir-phoenix.md) |
| Embedded Rust | 🟢 A | [`embedded-rust.md`](jobs/embedded-rust.md) |
| End-to-End Browser Testing | 🟢 A | [`e2e-browser-testing.md`](jobs/e2e-browser-testing.md) |
| Envoy — L7 Proxy & Edge | 🟢 A | [`envoy-proxy.md`](jobs/envoy-proxy.md) |
| Ethereum Smart Contracts | 🟢 A | [`ethereum-smart-contracts.md`](jobs/ethereum-smart-contracts.md) |
| Fast DataFrames (Polars/DuckDB) | 🟢 A | [`dataframes-polars-duckdb.md`](jobs/dataframes-polars-duckdb.md) |
| FastAPI Development | 🟢 A | [`fastapi-development.md`](jobs/fastapi-development.md) |
| Feature Stores | 🟢 A | [`feature-stores.md`](jobs/feature-stores.md) |
| FFmpeg — Audio/Video Processing | 🟢 A | [`ffmpeg-media.md`](jobs/ffmpeg-media.md) |
| Financial Analyst | 🔵 B | [`financial-analyst.md`](jobs/financial-analyst.md) |
| Fine-Tuning LLMs | 🟢 A | [`llm-finetuning.md`](jobs/llm-finetuning.md) |
| Flutter (Mobile) | 🟢 A | [`flutter-mobile.md`](jobs/flutter-mobile.md) |
| Frontend Frameworks | 🟢 A | [`frontend-frameworks.md`](jobs/frontend-frameworks.md) |
| Frontend State Management | 🟢 A | [`state-management-frontend.md`](jobs/state-management-frontend.md) |
| Fuzzing | 🟢 A | [`fuzzing.md`](jobs/fuzzing.md) |
| Game Engines — Unity & Unreal | 🟢 A | [`game-engine-unity-unreal.md`](jobs/game-engine-unity-unreal.md) |
| Geospatial & GIS | 🟢 A | [`geospatial-gis.md`](jobs/geospatial-gis.md) |
| Git & Version Control | 🟢 A | [`git-version-control.md`](jobs/git-version-control.md) |
| GitHub Actions — CI/CD | 🟢 A | [`github-actions-ci.md`](jobs/github-actions-ci.md) |
| GitOps — Argo CD & Flux | 🔵 B | [`gitops-argocd-flux.md`](jobs/gitops-argocd-flux.md) |
| Go Backend Libraries (frameworks & tooling) | 🔵 B | [`go-backend-libraries.md`](jobs/go-backend-libraries.md) |
| Go Development | 🟢 A | [`go-development.md`](jobs/go-development.md) |
| Go Testing | 🟢 A | [`go-testing.md`](jobs/go-testing.md) |
| Godot Game Engine | 🟢 A | [`godot-game-engine.md`](jobs/godot-game-engine.md) |
| Grafana — Dashboards & Visualization | 🟢 A | [`grafana-dashboards.md`](jobs/grafana-dashboards.md) |
| Graph Databases | 🟢 A | [`graph-databases.md`](jobs/graph-databases.md) |
| GraphQL APIs | 🟢 A | [`graphql-apis.md`](jobs/graphql-apis.md) |
| Headless CMS | 🔵 B | [`headless-cms.md`](jobs/headless-cms.md) |
| Helm — Kubernetes Package Manager | 🟢 A | [`helm-package-manager.md`](jobs/helm-package-manager.md) |
| Image Processing & Manipulation | 🟢 A | [`image-processing.md`](jobs/image-processing.md) |
| Infrastructure as Code — Terraform / OpenTofu | 🟢 A | [`terraform-iac.md`](jobs/terraform-iac.md) |
| Internationalization (i18n) | 🟢 A | [`i18n-localization.md`](jobs/i18n-localization.md) |
| IoT Messaging — MQTT | 🟢 A | [`iot-mqtt.md`](jobs/iot-mqtt.md) |
| Java Development | 🟢 A | [`java-development.md`](jobs/java-development.md) |
| JavaScript / TS Testing | 🔵 B | [`javascript-testing.md`](jobs/javascript-testing.md) |
| Jetpack Compose — Android | 🟢 A | [`jetpack-compose-android.md`](jobs/jetpack-compose-android.md) |
| Journalist / Newsroom | 🔵 B | [`journalist-newsroom.md`](jobs/journalist-newsroom.md) |
| JS Package Managers | 🔵 B | [`javascript-package-managers.md`](jobs/javascript-package-managers.md) |
| Kotlin Development | 🟢 A | [`kotlin-development.md`](jobs/kotlin-development.md) |
| Kotlin Multiplatform | 🟢 A | [`kotlin-multiplatform.md`](jobs/kotlin-multiplatform.md) |
| Kubernetes — Container Orchestration | 🟢 A | [`kubernetes-orchestration.md`](jobs/kubernetes-orchestration.md) |
| Lakehouse Tables — Delta & Iceberg | 🟢 A | [`delta-iceberg-lakehouse.md`](jobs/delta-iceberg-lakehouse.md) |
| Laravel / PHP Development | 🟢 A | [`laravel-php-development.md`](jobs/laravel-php-development.md) |
| Lawyer / Legal Work | 🔵 B | [`lawyer-legal-work.md`](jobs/lawyer-legal-work.md) |
| Learning English | 🔴 D | [`learning-english.md`](jobs/learning-english.md) |
| Learning Resources (general programming) | 🔵 B | [`learning-resources.md`](jobs/learning-resources.md) |
| Linux & Shell | 🔵 B | [`linux-shell.md`](jobs/linux-shell.md) |
| LLM App Development | 🟢 A | [`llm-app-development.md`](jobs/llm-app-development.md) |
| LLM Observability & Evals | 🟢 A | [`llm-observability-evals.md`](jobs/llm-observability-evals.md) |
| LLM Serving & Inference | 🟢 A | [`llm-serving-inference.md`](jobs/llm-serving-inference.md) |
| Load & Performance Testing | 🟢 A | [`load-testing.md`](jobs/load-testing.md) |
| Log Aggregation & Tracing | 🟢 A | [`log-aggregation.md`](jobs/log-aggregation.md) |
| Machine Learning (PyTorch) | 🟢 A | [`machine-learning-pytorch.md`](jobs/machine-learning-pytorch.md) |
| Markdown & Knowledge Tooling | 🟢 A | [`markdown-knowledge-tools.md`](jobs/markdown-knowledge-tools.md) |
| Marketer / Digital Marketing | 🔵 B | [`marketer-digital-marketing.md`](jobs/marketer-digital-marketing.md) |
| Message Queues & Streaming | 🟢 A | [`message-queues-streaming.md`](jobs/message-queues-streaming.md) |
| ML Data Apps (Streamlit/Gradio) | 🔵 B | [`ml-data-apps.md`](jobs/ml-data-apps.md) |
| ML Experiment Tracking | 🟢 A | [`experiment-tracking.md`](jobs/experiment-tracking.md) |
| Mobile Development | 🟢 A | [`mobile-development.md`](jobs/mobile-development.md) |
| Model Serving (non-LLM) | 🟢 A | [`model-serving-inference.md`](jobs/model-serving-inference.md) |
| MongoDB — Document Database | 🟢 A | [`mongodb-database.md`](jobs/mongodb-database.md) |
| Monorepo Tooling | 🔵 B | [`monorepo-tooling.md`](jobs/monorepo-tooling.md) |
| Multiplayer Game Networking | 🔵 B | [`game-networking-multiplayer.md`](jobs/game-networking-multiplayer.md) |
| Neovim / Vim | 🟢 A | [`neovim-vim-editor.md`](jobs/neovim-vim-editor.md) |
| Next.js — Full-Stack React | 🟢 A | [`nextjs-fullstack.md`](jobs/nextjs-fullstack.md) |
| Nginx & Web Servers | 🟢 A | [`nginx-web-servers.md`](jobs/nginx-web-servers.md) |
| NLP — Classic Text Processing | 🟢 A | [`nlp-spacy.md`](jobs/nlp-spacy.md) |
| Node.js Backend Frameworks | 🟢 A | [`nodejs-backend-frameworks.md`](jobs/nodejs-backend-frameworks.md) |
| Object Storage (S3) | 🟡 C | [`object-storage-s3.md`](jobs/object-storage-s3.md) |
| Observability & Monitoring | 🟢 A | [`observability-monitoring.md`](jobs/observability-monitoring.md) |
| Office Documents (Word / PDF / PowerPoint / Excel) | 🟢 A | [`office-documents.md`](jobs/office-documents.md) |
| ONNX — Model Interop & Optimization | 🟢 A | [`onnx-model-interop.md`](jobs/onnx-model-interop.md) |
| OpenTelemetry — Traces, Metrics, Logs | 🟢 A | [`opentelemetry-tracing.md`](jobs/opentelemetry-tracing.md) |
| Packer — Machine Image Building | 🟢 A | [`packer-images.md`](jobs/packer-images.md) |
| PDF Generation & Manipulation | 🟢 A | [`pdf-generation.md`](jobs/pdf-generation.md) |
| Phaser (Web Games) | 🟢 A | [`phaser-web-games.md`](jobs/phaser-web-games.md) |
| PostgreSQL — the Database, Deep | 🟢 A | [`postgresql-database.md`](jobs/postgresql-database.md) |
| Progressive Delivery — Canary & Blue/Green | 🔵 B | [`argo-rollouts-progressive-delivery.md`](jobs/argo-rollouts-progressive-delivery.md) |
| Project Manager | 🔵 B | [`project-manager.md`](jobs/project-manager.md) |
| Prometheus — Metrics & Alerting | 🟢 A | [`prometheus-monitoring.md`](jobs/prometheus-monitoring.md) |
| Prompt Engineering | 🟢 A | [`prompt-engineering.md`](jobs/prompt-engineering.md) |
| Property-Based Testing | 🟢 A | [`property-based-testing.md`](jobs/property-based-testing.md) |
| Protobuf & gRPC Schemas | 🟢 A | [`protobuf-grpc-schemas.md`](jobs/protobuf-grpc-schemas.md) |
| Pulumi — IaC in Real Languages | 🟢 A | [`pulumi-iac.md`](jobs/pulumi-iac.md) |
| PWAs & Service Workers | 🟢 A | [`pwa-service-workers.md`](jobs/pwa-service-workers.md) |
| PySpark — Distributed DataFrames | 🟢 A | [`spark-pyspark.md`](jobs/spark-pyspark.md) |
| Python Development | 🟢 A | [`python-development.md`](jobs/python-development.md) |
| Python ORMs & Query Builders | 🟢 A | [`orm-python.md`](jobs/orm-python.md) |
| Python Packaging & Environments | 🟢 A | [`python-packaging-uv.md`](jobs/python-packaging-uv.md) |
| Quantitative Finance & Backtesting | 🔵 B | [`quant-finance.md`](jobs/quant-finance.md) |
| RabbitMQ & NATS — Messaging | 🟢 A | [`rabbitmq-nats-messaging.md`](jobs/rabbitmq-nats-messaging.md) |
| RAG — Retrieval-Augmented Generation | 🟢 A | [`rag-retrieval.md`](jobs/rag-retrieval.md) |
| Rails Development | 🟢 A | [`rails-development.md`](jobs/rails-development.md) |
| React Development | 🟢 A | [`react-development.md`](jobs/react-development.md) |
| React Native (Mobile) | 🟢 A | [`react-native-mobile.md`](jobs/react-native-mobile.md) |
| Realtime — WebSockets & Pub/Sub | 🟢 A | [`realtime-websockets.md`](jobs/realtime-websockets.md) |
| Recommender Systems | 🔵 B | [`recommender-systems.md`](jobs/recommender-systems.md) |
| Recruiter / Talent Acquisition | 🔵 B | [`recruiter-talent-acquisition.md`](jobs/recruiter-talent-acquisition.md) |
| Redis — Caching & In-Memory Data | 🟢 A | [`redis-caching.md`](jobs/redis-caching.md) |
| Regular Expressions | 🟢 A | [`regular-expressions.md`](jobs/regular-expressions.md) |
| Release Automation & Versioning | 🟢 A | [`release-automation.md`](jobs/release-automation.md) |
| Reverse Proxy & Load Balancing | 🔵 B | [`reverse-proxy-load-balancing.md`](jobs/reverse-proxy-load-balancing.md) |
| Robotics — ROS 2 | 🟢 A | [`robotics-ros.md`](jobs/robotics-ros.md) |
| Rust Development | 🟢 A | [`rust-development.md`](jobs/rust-development.md) |
| SAST & Dependency Scanning | 🟢 A | [`sast-dependency-scanning.md`](jobs/sast-dependency-scanning.md) |
| Scalability & Distributed Systems | 🔵 B | [`scalability-distributed-systems.md`](jobs/scalability-distributed-systems.md) |
| Secrets Management (Vault) | 🟢 A | [`secrets-management-vault.md`](jobs/secrets-management-vault.md) |
| Service Mesh & Cloud Networking | 🟢 A | [`service-mesh-networking.md`](jobs/service-mesh-networking.md) |
| Social Media Research | 🔵 B | [`social-media-research.md`](jobs/social-media-research.md) |
| Software Design Patterns | 🟡 C | [`software-design-patterns.md`](jobs/software-design-patterns.md) |
| Speech — STT & TTS | 🟢 A | [`speech-stt-tts.md`](jobs/speech-stt-tts.md) |
| Spring Boot Development | 🟢 A | [`spring-boot-development.md`](jobs/spring-boot-development.md) |
| SQL Databases — MySQL & SQLite | 🟢 A | [`sql-databases-mysql.md`](jobs/sql-databases-mysql.md) |
| SQLite & Embedded Databases | 🟢 A | [`sqlite-embedded.md`](jobs/sqlite-embedded.md) |
| Static Site & Docs Generators | 🟢 A | [`static-site-generators.md`](jobs/static-site-generators.md) |
| Stream Processing | 🟢 A | [`stream-processing.md`](jobs/stream-processing.md) |
| Stripe — Payments Integration | 🟢 A | [`stripe-payments.md`](jobs/stripe-payments.md) |
| SwiftUI — iOS / Apple Apps | 🟢 A | [`swiftui-ios.md`](jobs/swiftui-ios.md) |
| Systems Programming (C / C++ / Zig) | 🟢 A | [`systems-programming-c-cpp-zig.md`](jobs/systems-programming-c-cpp-zig.md) |
| Tailwind CSS — Utility-First Styling | 🟢 A | [`tailwind-css.md`](jobs/tailwind-css.md) |
| Teacher / Educator | 🔵 B | [`teacher-educator.md`](jobs/teacher-educator.md) |
| Technical Interview Prep | 🔵 B | [`interview-prep.md`](jobs/interview-prep.md) |
| Terminal Power Tools | 🟢 A | [`terminal-shell-tools.md`](jobs/terminal-shell-tools.md) |
| Time-Series Databases | 🟢 A | [`timeseries-databases.md`](jobs/timeseries-databases.md) |
| Time-Series Forecasting | 🟢 A | [`timeseries-forecasting.md`](jobs/timeseries-forecasting.md) |
| TLS Certificates & HTTPS | 🟢 A | [`tls-certificates.md`](jobs/tls-certificates.md) |
| Transactional Email & Templates | 🟢 A | [`email-transactional.md`](jobs/email-transactional.md) |
| Translator / Localization Specialist | 🔵 B | [`translator-localization.md`](jobs/translator-localization.md) |
| Trino / Presto — Federated SQL | 🟢 A | [`trino-presto-query.md`](jobs/trino-presto-query.md) |
| TypeScript & JavaScript | 🟢 A | [`typescript-javascript.md`](jobs/typescript-javascript.md) |
| TypeScript ORMs | 🔵 B | [`typescript-orm.md`](jobs/typescript-orm.md) |
| Upwork Freelancing | 🟢 A | [`upwork.md`](jobs/upwork.md) |
| Vector Databases — Semantic Search | 🟢 A | [`vector-databases.md`](jobs/vector-databases.md) |
| Velero — Kubernetes Backup & DR | 🟢 A | [`velero-backup.md`](jobs/velero-backup.md) |
| Vetting Agent Skills & LLM Security | 🟢 A | [`agent-skill-security.md`](jobs/agent-skill-security.md) |
| Vite — Frontend Build Tooling | 🟢 A | [`vite-build-tooling.md`](jobs/vite-build-tooling.md) |
| Vue & Svelte Development | 🟢 A | [`vue-svelte-development.md`](jobs/vue-svelte-development.md) |
| Web / Frontend Development | 🟢 A | [`web-frontend.md`](jobs/web-frontend.md) |
| Web Animation & Motion | 🟢 A | [`web-animation.md`](jobs/web-animation.md) |
| Web Forms & Schema Validation | 🟢 A | [`forms-validation-web.md`](jobs/forms-validation-web.md) |
| Web Pentest & DAST | 🟢 A | [`dast-web-pentest.md`](jobs/dast-web-pentest.md) |
| Web Scraping & Crawling | 🟢 A | [`web-scraping.md`](jobs/web-scraping.md) |
| Web3 Frontend & Wallet Integration | 🟢 A | [`blockchain-web3-frontend.md`](jobs/blockchain-web3-frontend.md) |
| WebAssembly | 🟢 A | [`wasm-webassembly.md`](jobs/wasm-webassembly.md) |
| Whiteboard & Canvas Apps | 🔵 B | [`whiteboard-canvas-apps.md`](jobs/whiteboard-canvas-apps.md) |
| Workflow Automation (n8n) | 🟢 A | [`workflow-automation-n8n.md`](jobs/workflow-automation-n8n.md) |
| Zig Language | 🟢 A | [`zig-language.md`](jobs/zig-language.md) |

---

*Curated index. Skills remain the property of their original authors under their own
licenses. This repo claims no ownership of linked skills — only the trust assessment.*
