#!/usr/bin/python

import os, sys, subprocess

def make_path(*nodes):
    return os.path.join(*nodes)

def make_fake_bundle(bundle_path):
    storybook_path = make_path(bundle_path, 'movies', 'cutscenes', 'storybook')
    os.makedirs(storybook_path, exist_ok=True)

    for i in range(1, 24):
        filename = 'st_{id}.usm'.format(id = i)
        open(make_path(storybook_path, filename), 'w')

def run_quickbms(bundles_path, fake_bundles_path):
    subprocess.run([
        'quickbms',
        '-G',
        '-w',
        '-r',
        'witcher3.bms',
        make_path(bundles_path, 'movies.bundle'),
        fake_bundles_path
    ])

def main(argv):
    if len(argv) < 1:
        print("Usage: python no_flashbacks.py [path to Witcher 3 root directory] [path to quickbms directory]")
        sys.exit(2)

    root_path = argv[0]
    bundles_path = make_path(root_path, 'content', 'content0', 'bundles')
    fake_bundles_path = make_path(bundles_path, '__no-flashbacks__', 'bundles')

    make_fake_bundle(fake_bundles_path)
    run_quickbms(bundles_path, fake_bundles_path)

if __name__ == "__main__":
    main(sys.argv[1:])
