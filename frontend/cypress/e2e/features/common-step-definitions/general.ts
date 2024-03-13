// eslint-disable-next-line @typescript-eslint/no-unused-vars
import { Given, Then, When } from "@badeball/cypress-cucumber-preprocessor";

When("os cookies são limpos", () => {
    window.localStorage.clear()
});