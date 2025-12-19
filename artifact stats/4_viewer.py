import tkinter as tk
from tkinter import ttk
import pandas as pd

# Load your artifact data
df = pd.read_csv("artifacts.csv")

root = tk.Tk()
root.title("Genshin Artifact Inventory")
root.geometry("1500x800")

# --- Frames ---
top_frame = tk.Frame(root)
top_frame.pack(side="top", fill="x", padx=10, pady=5)

# Scrollable canvas for artifact grid
canvas = tk.Canvas(root, width=1100, height=700)
canvas.pack(side="left", fill="both", expand=True)

scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
scrollbar.pack(side="left", fill="y")

canvas.configure(yscrollcommand=scrollbar.set)

# Frame inside the canvas
grid_frame = tk.Frame(canvas)
canvas.create_window((0, 0), window=grid_frame, anchor="nw")

# Right panel for details
details_frame = tk.Frame(root, width=350, relief="solid", bd=2)
details_frame.pack(side="right", fill="y", padx=10, pady=10)

artifact_details = tk.Label(details_frame, text="Select an artifact", justify="left", anchor="nw", font=("Arial", 12))
artifact_details.pack(fill="both", expand=True, padx=10, pady=10)


# --- Function to update scroll region ---
def on_frame_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))


grid_frame.bind("<Configure>", on_frame_configure)


# --- Function to show details of selected artifact ---
def show_artifact_details(idx):
    artifact = filtered_df.iloc[idx]

    subs = []
    for i in range(1, 5):
        stat_col = f"Sub Stat {i}"
        val_col = f"Sub Stat Value {i}"
        if pd.notna(artifact[stat_col]) and pd.notna(artifact[val_col]):
            subs.append(f"{artifact[stat_col]} +{artifact[val_col]}")

    score_cols = [c for c in df.columns if "score" in c.lower()]
    best_score = artifact[score_cols].max()

    text = (
        f"Set: {artifact['Set']}\n"
        f"Slot: {artifact['Slot']}\n"
        f"Rarity: {artifact['Stars']}★\n"
        f"Level: +{artifact['Level']}\n"
        f"Main Stat: {artifact['Main Stat']} +{artifact['Main Stat Value']}\n\n"
        f"Substats:\n  " + "\n  ".join(subs) + "\n\n"
        f"Best Score: {best_score:.2f}"
    )
    artifact_details.config(text=text)


# --- Function to refresh grid with filter ---
def refresh_grid(*args):
    for widget in grid_frame.winfo_children():
        widget.destroy()

    selected_set = set_filter_var.get()
    global filtered_df
    if selected_set == "All":
        filtered_df = df
    else:
        filtered_df = df[df["Set"] == selected_set]

    score_cols = [c for c in df.columns if "score" in c.lower()]

    for idx, (i, artifact) in enumerate(filtered_df.iterrows()):
        label = f"{artifact['Slot']} ({artifact['Stars']}★)\n+{artifact['Level']}"

        best_score = artifact[score_cols].max()
        color = "SystemButtonFace"
        if best_score < 25:
            color = "red"

        btn = tk.Button(
            grid_frame,
            text=label,
            width=12,
            height=4,
            bg=color,
            command=lambda idx=idx: show_artifact_details(idx)
        )
        row, col = divmod(idx, 8)
        btn.grid(row=row, column=col, padx=3, pady=3)


# --- Filter dropdown ---
set_filter_var = tk.StringVar()
set_names = ["All"] + sorted(df["Set"].dropna().unique())
set_filter = ttk.Combobox(top_frame, textvariable=set_filter_var, values=set_names, state="readonly")
set_filter_var.set("All")
set_filter.pack(side="left")

set_filter.bind("<<ComboboxSelected>>", refresh_grid)

# --- Initial load ---
filtered_df = df
refresh_grid()

root.mainloop()
