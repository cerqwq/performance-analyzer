"""
Performance Analyzer - AI性能分析工具
支持代码性能分析、瓶颈识别、优化建议
"""

import json
import os
from typing import Dict, List, Any
from datetime import datetime

try:
    from openai import OpenAI
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False


class PerformanceAnalyzer:
    """
    AI性能分析工具
    支持：性能分析、瓶颈识别、优化建议
    """

    def __init__(self, model: str = "mimo-v2.5-pro", api_key: str = None, base_url: str = None):
        self.model = model
        if OPENAI_AVAILABLE:
            self.client = OpenAI(
                api_key=api_key or os.environ.get('OPENAI_API_KEY', ''),
                base_url=base_url or os.environ.get('OPENAI_BASE_URL', 'https://api.xiaomimimo.com/v1')
            )
        else:
            self.client = None

    def analyze_code(self, code: str, language: str = "Python") -> Dict:
        """分析代码性能"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        prompt = f"""请分析以下{language}代码的性能：

```{language}
{code}
```

请返回JSON格式：
{{
    "complexity": {{"time": "O(n)", "space": "O(n)"}},
    "bottlenecks": [
        {{"location": "位置", "issue": "问题", "impact": "影响", "optimization": "优化建议"}}
    ],
    "score": 1-10,
    "recommendations": ["建议1", "建议2"]
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=2000
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"analysis": content}

    def optimize_code(self, code: str, language: str = "Python") -> str:
        """优化代码"""
        if not self.client:
            return "LLM客户端未配置"

        prompt = f"""请优化以下{language}代码的性能：

```{language}
{code}
```

要求：
1. 保持功能不变
2. 提高执行效率
3. 减少内存使用
4. 添加优化说明注释"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=2000
        )

        return response.choices[0].message.content

    def analyze_database_query(self, query: str, schema: str = "") -> Dict:
        """分析数据库查询性能"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        prompt = f"""请分析以下SQL查询的性能：

Schema：{schema}

查询：{query}

请返回JSON格式：
{{
    "issues": ["问题1", "问题2"],
    "optimizations": ["优化1", "优化2"],
    "indexes": ["建议索引1", "建议索引2"],
    "estimated_improvement": "预期提升"
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1000
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"query_analysis": content}

    def analyze_api_performance(self, endpoint: str, response_time: float, payload_size: int) -> Dict:
        """分析API性能"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        prompt = f"""请分析以下API的性能：

端点：{endpoint}
响应时间：{response_time}ms
负载大小：{payload_size} bytes

请返回JSON格式：
{{
    "status": "good/warning/critical",
    "issues": ["问题1", "问题2"],
    "optimizations": ["优化1", "优化2"],
    "best_practices": ["建议1", "建议2"]
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1000
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"api_analysis": content}

    def generate_load_test(self, endpoint: str, concurrency: int = 10, duration: int = 60) -> str:
        """生成负载测试脚本"""
        if not self.client:
            return "LLM客户端未配置"

        prompt = f"""请为以下API生成负载测试脚本：

端点：{endpoint}
并发数：{concurrency}
持续时间：{duration}秒

请使用locust框架生成Python测试脚本："""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=2000
        )

        return response.choices[0].message.content


def create_analyzer(**kwargs) -> PerformanceAnalyzer:
    """创建性能分析器"""
    return PerformanceAnalyzer(**kwargs)


if __name__ == "__main__":
    analyzer = create_analyzer()

    print("Performance Analyzer")
    print()

    # 测试代码
    test_code = """
def find_duplicates(lst):
    duplicates = []
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] == lst[j] and lst[i] not in duplicates:
                duplicates.append(lst[i])
    return duplicates
"""

    result = analyzer.analyze_code(test_code, "Python")
    print(json.dumps(result, ensure_ascii=False, indent=2))
