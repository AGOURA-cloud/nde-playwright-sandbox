const { test, expect } = require('@playwright/test');
const { resolve } = require('node:path');
const { pathToFileURL } = require('node:url');

test('add alpha, count one, reset zero', async ({ page }) => {
  await page.goto(pathToFileURL(resolve(__dirname, 'fixture.html')).href);
  await page.getByRole('button', { name: 'Add' }).click();
  await expect(page.getByRole('listitem')).toHaveText('alpha');
  await expect(page.locator('#count')).toHaveText('Items: 1');
  await page.getByRole('button', { name: 'Reset' }).click();
  await expect(page.getByRole('listitem')).toHaveCount(0);
  await expect(page.locator('#count')).toHaveText('Items: 0');
});
