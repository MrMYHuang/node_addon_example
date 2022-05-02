{
    'targets': [
        {
            'target_name': 'hello',
            'sources': [
                'src/hello.cpp'
            ],
            'include_dirs': ["<!(node -p \"require('node-addon-api').include_dir\")"],
            'cflags!': ['-fno-exceptions'],
            'cflags_cc!': ['-fno-exceptions'],
            'conditions': [
                ["OS=='win'", {
                    "defines": [
                        "_HAS_EXCEPTIONS=1"
                    ],
                    "msvs_settings": {
                        "VCCLCompilerTool": {
                            "ExceptionHandling": 1
                        },
                    },
                }],
                ["OS=='mac'", {
                    'cflags+': ['-fvisibility=hidden'],
                    'xcode_settings': {
                        'GCC_ENABLE_CPP_EXCEPTIONS': 'YES',
                        'GCC_SYMBOLS_PRIVATE_EXTERN': 'YES',
                        'CLANG_CXX_LIBRARY': 'libc++',
                        'MACOSX_DEPLOYMENT_TARGET': '10.7',
                    },
                }],
            ],
        }
    ]
}
