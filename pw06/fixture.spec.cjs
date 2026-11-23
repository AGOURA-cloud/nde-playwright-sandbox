const { test, expect } = require('@playwright/test');
const { resolve } = require('node:path');
const { pathToFileURL } = require('node:url');

test.beforeEach(async ({ page }) => {
  await page.goto(pathToFileURL(resolve(__dirname, 'fixture.html')).href);
});

test('add one item and reset to zero', async ({ page }) => {
  await expect(page.locator('#count')).toHaveText('Items: 0');
  await page.getByRole('button', { name: 'Add' }).click();
  await expect(page.getByRole('listitem')).toHaveText('alpha');
  await expect(page.locator('#count')).toHaveText('Items: 1');
  await page.getByRole('button', { name: 'Reset' }).click();
  await expect(page.getByRole('listitem')).toHaveCount(0);
  await expect(page.locator('#count')).toHaveText('Items: 0');
});

test('multiple adds count accurately', async ({ page }) => {
  await page.getByRole('textbox', { name: 'New item' }).fill('first');
  await page.getByRole('button', { name: 'Add' }).click();
  await page.getByRole('textbox', { name: 'New item' }).fill('second');
  await page.getByRole('button', { name: 'Add' }).click();
  await expect(page.getByRole('listitem')).toHaveText(['first', 'second']);
  await expect(page.locator('#count')).toHaveText('Items: 2');
});

test('reset empty list is safe, and add works afterward', async ({ page }) => {
  await page.getByRole('button', { name: 'Reset' }).click();
  await expect(page.getByRole('listitem')).toHaveCount(0);
  await expect(page.locator('#count')).toHaveText('Items: 0');
  await page.getByRole('button', { name: 'Add' }).click();
  await expect(page.getByRole('listitem')).toHaveText('alpha');
  await expect(page.locator('#count')).toHaveText('Items: 1');
});
