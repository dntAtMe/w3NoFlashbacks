#!/usr/bin/python

import os, sys, subprocess, argparse

def make_parser():
    parser = argparse.ArgumentParser(
        prog = 'w3NoFlashbacks',
        description = 'Removes all retrospective cutscenes from Witcher 3',
        epilog = 'This script requires QuickBMS as a dependency; Please note it assumes witcher3.bms script is in the same directory as quickbms executable.')

    parser.add_argument('--game', '-g', help = 'Path to Witcher 3 root directory', default='.', dest='game_path')
    parser.add_argument('--quickbms', '-q', help = 'Path to QuickBMS directory', default='.', dest='quickbms_path')

    return parser


def make_path(*nodes):
    return os.path.join(*nodes)

def make_fake_bundle(bundle_path):
    storybook_path = make_path(bundle_path, 'movies', 'cutscenes', 'storybook')
    os.makedirs(storybook_path, exist_ok=True)

    for i in range(1, 24):
        filename = 'st_{id}.usm'.format(id = i)
        open(make_path(storybook_path, filename), 'w')

def run_quickbms(quickbms_path, bundles_path, fake_bundles_path):
    subprocess.run([
        make_path(quickbms_path, 'quickbms'),
        '-G',
        '-w',
        '-r',
        'witcher3.bms',
        make_path(bundles_path, 'movies.bundle'),
        fake_bundles_path
    ])

def main():
    parser = make_parser()
    args = parser.parse_args()

    assert(os.path.exists(make_path(args.game_path, 'bin', 'x64', 'witcher3.exe'))), \
        'Witcher 3 executable not found in game directory, please make sure it is the correct directory.'
    assert(os.path.exists(make_path(args.quickbms_path, 'quickbms.exe'))), \
        'QuickBMS executable not found in QuickBMS directory.'
    assert(os.path.exists(make_path(args.quickbms_path, 'witcher3.bms'))), \
        'witcher3.bms script not found in QuickBMS directory.'

    bundles_path = make_path(args.game_path, 'content', 'content0', 'bundles')
    fake_bundles_path = make_path(bundles_path, '__no-flashbacks__', 'bundles')

    make_fake_bundle(fake_bundles_path)
    run_quickbms(args.quickbms_path, bundles_path, fake_bundles_path)

if __name__ == "__main__":
    main()
