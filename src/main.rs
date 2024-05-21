use bevy::{
    prelude::*,
    sprite::{MaterialMesh2dBundle, Mesh2dHandle},
    window::*,
    core::FrameCount,
};

mod plugins;

use plugins::{
    node::NodePlugin,
    camera::CameraPlugin,
};

fn main() {
    App::new()
        .add_plugins(
            DefaultPlugins
                .set(ImagePlugin::default_nearest())
                .set(WindowPlugin {
                    primary_window: Some(Window {
                        title: "Lights Out".into(),
                        resolution: (800.0, 600.0).into(),
                        window_theme: Some(WindowTheme::Dark),
                        present_mode: PresentMode::AutoVsync,
                        visible: false,
                        ..default()
                    }),
                    ..default()
                })
                .build(),
        )
        .add_systems(
            Update,
            (
                make_visible,
            ),
        )
        .add_plugins((CameraPlugin, NodePlugin))
        .run();
}

fn make_visible(
    mut window: Query<&mut Window>, 
    frames: Res<FrameCount>
) {
    if frames.0 == 3 {
        window.single_mut().visible = true;
    }
}

