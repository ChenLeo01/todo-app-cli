# Todo App CLI

[English](./README.md) | [中文](./README.zh-CN.md)

一个使用 Python 构建的简单命令行待办事项管理工具。

这个项目允许用户直接在终端中管理任务。任务会被保存在本地的 JSON 文件中，因此即使程序退出，任务数据也不会丢失。

## 项目简介

这是一个适合 Python 初学者练习的项目，主要用于巩固以下基础知识：

- 使用 `argparse` 解析命令行参数
- 文件读取与写入
- 使用 JSON 存储数据
- 函数与模块化逻辑
- 列表和字典的使用
- 错误处理
- 基础命令行应用程序设计

## 功能

- 添加新任务
- 设置任务优先级：`High`、`Medium` 或 `Low`
- 查看所有任务
- 将任务标记为已完成
- 根据序号删除任务
- 根据关键词搜索任务
- 清除所有已完成任务
- 清空整个任务列表
- 自动将任务保存到本地 JSON 文件中

## 使用技术

- Python 3
- `argparse`
- `json`
- `os`

本项目不需要安装任何第三方库。

## 项目结构

```text
todo-cli-app/
│
├── todo_cli.py
├── tasks.json
└── README.md
```

## 如何运行

首先，确保你已经进入项目文件夹：

```bash
cd todo-cli-app
```

然后使用以下格式运行命令：

```bash
python3 todo_cli.py <command>
```

## 命令说明

### 添加任务

```bash
python3 todo_cli.py add learn python argparse
```

添加带有优先级的任务：

```bash
python3 todo_cli.py add learn python argparse --priority High
```

可用的优先级包括：

```text
High
Medium
Low
```

如果没有指定优先级，默认优先级为 `Medium`。

### 查看所有任务

```bash
python3 todo_cli.py list
```

示例输出：

```text
index   status  description             priority
1.      ❎      learn python argparse    High
2.      ✅      review json              Medium
```

### 将任务标记为完成

```bash
python3 todo_cli.py done 1
```

这会将序号为 `1` 的任务标记为已完成。

### 删除任务

```bash
python3 todo_cli.py delete 1
```

这会删除序号为 `1` 的任务。

### 搜索任务

```bash
python3 todo_cli.py search python
```

这会搜索包含关键词 `python` 的任务。

### 清除已完成任务

```bash
python3 todo_cli.py clear
```

这会删除所有已经被标记为完成的任务。

### 清空所有任务

```bash
python3 todo_cli.py empty
```

这会清空整个任务列表。

## 数据存储

任务会被保存在本地 JSON 文件中：

```text
tasks.json
```

每个任务都会以字典的形式存储，结构如下：

```json
{
  "description": "learn python argparse",
  "done": false,
  "priority": "High"
}
```

## 示例流程

```bash
python3 todo_cli.py add learn python functions --priority High
python3 todo_cli.py add practice json file storage
python3 todo_cli.py list
python3 todo_cli.py done 1
python3 todo_cli.py search python
python3 todo_cli.py clear
python3 todo_cli.py list
```

## 我的收获

通过这个项目，我练习了几个重要的 Python 基础知识：

- 如何使用 `argparse` 构建命令行工具
- 如何使用 JSON 存储和读取数据
- 如何使用函数拆分程序逻辑
- 如何处理用户输入和无效数据
- 如何使用列表和字典管理数据
- 如何构建一个小型但实用的 Python 应用程序

这个项目也帮助我理解了基础的任务管理逻辑。对于之后学习 AI Agent 项目也有帮助，因为 Agent 经常需要创建、管理和追踪任务。

## 未来改进方向

之后可以考虑加入以下功能：

- 添加任务截止日期
- 按优先级排序任务
- 按任务状态筛选任务
- 添加任务分类
- 改进损坏 JSON 文件时的错误处理
- 将项目拆分成多个 Python 文件
- 同时支持交互式 CLI 模式和命令行参数模式
