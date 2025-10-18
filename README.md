# codesahayakcodesahayak/
├── README.md
├── requirements.txt
├── .env.example
├── .gitignore
├── friction_log.md
├── demo/
│   └── demo_video.mp4
├── src/
│   ├── __init__.py
│   ├── main.py                 # Main agent orchestrator
│   ├── agents/
│   │   ├── __init__.py
│   │   ├── voice_agent.py      # Voice input/output handler
│   │   ├── code_analyzer.py    # Code review agent
│   │   ├── learning_manager.py # Progress tracking agent
│   │   └── coordinator.py      # Multi-tool orchestrator
│   ├── tools/
│   │   ├── __init__.py
│   │   └── composio_tools.py   # Composio Tool Router integration
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── voice_utils.py      # Whisper + ElevenLabs
│   │   └── code_parser.py      # AST parsing utilities
│   └── config/
│       ├── __init__.py
│       └── settings.py         # Configuration management
└── tests/
    ├── __init__.py
    ├── test_voice.py
    ├── test_analyzer.py
    └── test_workflow.py
