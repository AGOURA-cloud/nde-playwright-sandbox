const { test, expect } = require('@playwright/test');
const { pathToFileURL } = require('node:url');
const path = require('node:path');

test('GitHub runner launches Chromium and verifies add/reset', async ({ page }) => {
  await page.goto(pathToFileURL(path.resolve(__dirname, 'fixture.html')).href);
  await expect(page.getByText('Items: 0')).toBeVisible();
  await page.getByRole('button', { name: 'Add' }).click();
  await expect(page.getByRole('listitem')).toHaveText('alpha');
  await expect(page.getByText('Items: 1')).toBeVisible();
  await page.getByRole('button', { name: 'Reset' }).click();
  await expect(page.getByText('Items: 0')).toBeVisible();
});