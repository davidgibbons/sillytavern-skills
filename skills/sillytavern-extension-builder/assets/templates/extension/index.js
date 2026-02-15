import {
    extension_settings,
    loadExtensionSettings,
    renderExtensionTemplateAsync,
    getContext,
} from '../../../extensions.js';
import { eventSource, event_types, saveSettingsDebounced } from '../../../../script.js';

const EXTENSION_NAME = '__EXT_SLUG__';
const defaultSettings = {
    enabled: true,
    debug: false,
};

extension_settings[EXTENSION_NAME] = extension_settings[EXTENSION_NAME] || {};
const settings = Object.assign({}, defaultSettings, extension_settings[EXTENSION_NAME]);
extension_settings[EXTENSION_NAME] = settings;

function saveSettings() {
    saveSettingsDebounced();
}

function bindSettingsUi() {
    $('#__EXT_SLUG___enabled').prop('checked', settings.enabled);
    $('#__EXT_SLUG___debug').prop('checked', settings.debug);

    $('#__EXT_SLUG___enabled').on('change', function () {
        settings.enabled = Boolean($(this).prop('checked'));
        saveSettings();
    });

    $('#__EXT_SLUG___debug').on('change', function () {
        settings.debug = Boolean($(this).prop('checked'));
        saveSettings();
    });
}

async function renderSettings() {
    const html = await renderExtensionTemplateAsync(EXTENSION_NAME, 'settings');
    $('#extensions_settings2').append(html);
    bindSettingsUi();
}

function onAppReady() {
    if (settings.debug) {
        console.log(`[${EXTENSION_NAME}] app ready`);
    }
}

function onGenerationAfterCommands() {
    if (!settings.enabled) {
        return;
    }

    const context = getContext();
    if (settings.debug) {
        console.log(`[${EXTENSION_NAME}] generation hook`, context?.chatId);
    }
}

jQuery(async () => {
    await loadExtensionSettings(EXTENSION_NAME);
    await renderSettings();

    eventSource.on(event_types.APP_READY, onAppReady);
    eventSource.on(event_types.GENERATION_AFTER_COMMANDS, onGenerationAfterCommands);
});
