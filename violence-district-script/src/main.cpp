#include <iostream>
#include "roblox_utils.h"
#include "script_hooks.h"

int main() {
    if (!RobloxUtils::isInGame()) {
        std::cerr << "Not in a Roblox game!" << std::endl;
        return 1;
    }

    std::cout << "Current place ID: " << RobloxUtils::getCurrentPlaceId() << std::endl;
    ScriptHooks::injectViolenceDistrictScript();
    ScriptHooks::setupAutoRespawn();
    ScriptHooks::enableGodMode();

    return 0;
}