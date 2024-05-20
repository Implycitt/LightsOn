use sdl2::event::Event;
use crate::winsdl::Winsdl;

mod winsdl;

fn main() {
    let mut winsdl = Winsdl::new(800, 600).unwrap();

    'running: loop {
        for event in winsdl.event_pump.poll_iter() {
            match event {
                Event::Quit { .. } => break 'running,
                _ => { }
            }
        }

        unsafe {
            gl::ClearColor(0.3, 0.3, 0.3, 1.0);
            gl::Clear(gl::COLOR_BUFFER_BIT);
        }
        
        winsdl.window.gl_swap_window();
    }
}
