# ⚡ Performance Analyzer

AI性能分析工具，支持代码性能分析、瓶颈识别、优化建议。

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python" />
  <img src="https://img.shields.io/badge/OpenAI-API-green?logo=openai" />
  <img src="https://img.shields.io/badge/License-MIT-yellow" />
</p>

## ✨ 特性

- 📊 代码性能分析
- 🔍 瓶颈识别
- ⚡ 代码优化
- 🗄️ SQL查询分析
- 🌐 API性能分析
- 🔧 负载测试生成

## 🚀 快速开始

```bash
pip install openai

python analyzer.py
```

## 📖 使用

```python
from performance_analyzer import create_analyzer

analyzer = create_analyzer()

# 分析代码
result = analyzer.analyze_code(code, "Python")

# 优化代码
optimized = analyzer.analyze_code(code, "Python")

# 分析SQL查询
query_result = analyzer.analyze_database_query(sql, schema)

# 分析API性能
api_result = analyzer.analyze_api_performance("/api/users", 200, 1024)

# 生成负载测试
test_script = analyzer.generate_load_test("/api/users", 100, 60)
```

## 📁 项目结构

```
performance-analyzer/
├── analyzer.py    # 性能分析器核心
└── README.md
```

## 📄 许可证

MIT License
