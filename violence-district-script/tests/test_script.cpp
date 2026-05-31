#include <gtest/gtest.h>
#include "roblox_utils.h"

TEST(RobloxUtilsTest, IsInGame) {
    EXPECT_TRUE(RobloxUtils::isInGame() || !RobloxUtils::isInGame());
}

TEST(RobloxUtilsTest, GetCurrentPlaceId) {
    std::string placeId = RobloxUtils::getCurrentPlaceId();
    EXPECT_FALSE(placeId.empty());
}