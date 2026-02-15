import {
    extension_settings,
    loadExtensionSettings,
    renderExtensionTemplateAsync,
} from '../../../extensions.js';
import { eventSource, event_types, saveSettingsDebounced } from '../../../../script.js';

const EXTENSION_NAME = '__EXT_SLUG__';
const COMMAND_NAME = '__EXT_SLUG__';
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

async function importFromUrl(url) {
    const module = await import(url);
    return module;
}

async function registerSlashCommand() {
    const [{ SlashCommandParser }, { SlashCommand }, { SlashCommandArgument, SlashCommandNamedArgument, ARGUMENT_TYPE }] =
        await Promise.all([
            importFromUrl('/scripts/slash-commands/SlashCommandParser.js'),
            importFromUrl('/scripts/slash-commands/SlashCommand.js'),
            importFromUrl('/scripts/slash-commands/SlashCommandArgument.js'),
        ]);

    SlashCommandParser.addCommandObject(
        SlashCommand.fromProps({
            name: COMMAND_NAME,
            helpString: `${COMMAND_NAME} <text>: echo text through the extension`,
            unnamedArgumentList: [
                SlashCommandArgument.fromProps({
                    description: 'Text to echo',
                    typeList: [ARGUMENT_TYPE.STRING],
                    isRequired: true,
                }),
            ],
            namedArgumentList: [
                SlashCommandNamedArgument.fromProps({
                    name: 'upper',
                    description: 'Transform output to uppercase',
                    typeList: [ARGUMENT_TYPE.BOOLEAN],
                    defaultValue: 'false',
                    forceEnum: false,
                    isRequired: false,
                }),
            ],
            callback: async (args, rawText) => {
                if (!settings.enabled) {
                    return `[${EXTENSION_NAME}] disabled`;
                }

                const source = (rawText || '').trim();
                if (!source) {
                    return `/${COMMAND_NAME} requires text`;
                }

                const upper = String(args.upper || 'false').toLowerCase() === 'true';
                const output = upper ? source.toUpperCase() : source;
                return `[${EXTENSION_NAME}] ${output}`;
            },
        }),
    );
}

async function onAppReady() {
    await registerSlashCommand();
    if (settings.debug) {
        console.log(`[${EXTENSION_NAME}] slash command /${COMMAND_NAME} registered`);
    }
}

jQuery(async () => {
    await loadExtensionSettings(EXTENSION_NAME);
    await renderSettings();
    eventSource.on(event_types.APP_READY, onAppReady);
});
