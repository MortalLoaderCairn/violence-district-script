#pragma once
#include <string>

namespace RobloxUtils {
    bool isInGame();
    std::string getCurrentPlaceId();
    void executeScript(const std::string& script);
}