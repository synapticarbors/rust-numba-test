#![crate_type = "dylib"]

#[no_mangle]
pub extern fn rust_double_callback(cb: extern "C" fn(i64) -> f64, n: i64) -> f64 { 
    2.0 * cb(n)
}
