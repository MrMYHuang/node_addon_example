#include "napi.h"

Napi::Object Init(Napi::Env env, Napi::Object exports)
{
    exports.Set(Napi::String::New(env, "hello"), Napi::String::New(env, "world"));
    return exports;
}

NODE_API_MODULE(NODE_GYP_MODULE_NAME, Init)
