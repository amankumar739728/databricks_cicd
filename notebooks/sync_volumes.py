# Databricks notebook source

# Sync all files from dev volume to stg and prod volumes
src = "/Volumes/dev_catalog/dev_schema/data/"
targets = [
    "/Volumes/stg_catalog/stg_schema/data/",
    "/Volumes/prod_catalog/prod_schema/data/"
]

files = dbutils.fs.ls(src)
print(f"Found {len(files)} files in dev volume")

for f in files:
    for target in targets:
        dest = target + f.name
        dbutils.fs.cp(f.path, dest, recurse=False)
        print(f"✓ Copied {f.name} → {target}")

print("Sync completed!")